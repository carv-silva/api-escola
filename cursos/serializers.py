from rest_framework import serializers
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            # o email nao vai ser apresentado qnd alguem consultar
            'email': {'write_only': True}
        }
        model = Avaliacao
        #  campos para mostrar pro usuario
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )


class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationsship
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLinked Related Field Da um link das avaliacoes para evitar muitos dados na pagina
    avaliacoes = serializers.HyperlinkedRelatedField(many=True,
                                                     read_only=True,

                                                     view_name='avaliacao-detail')

    """
    # Primary Key Related Field Ele da uma lista das avaliacoes somente por id, nao tem link
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True,
                                                    read_only=True,
                                                    view_name='avaliacao-detail')
    """

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )


# string binaria é bem mais rapido que uma string normal, ela comeca com b'
