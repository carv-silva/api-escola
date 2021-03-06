from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Curso(Base):
    titulo = models.CharField(max_length=255)
    # o unique serve para nao criar duas url com mesmo valor
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id']

    def __str__(self):
        return self.titulo


class Avaliacao(Base):
    curso = models.ForeignKey(
        Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    # nao é obrigatorio qnd usa blank
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(
        max_digits=2, decimal_places=1)  # notas quebradas

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        # usado para qnd é 2 unicos para avaliar
        unique_together = ['email', 'curso']
        ordering = ['id']  # se vc colocar -id é ordem decrescente

        def __str__(self):
            return f'{self.nome} avaliou o curso {self.curso} com nota {self.avalicao}'
