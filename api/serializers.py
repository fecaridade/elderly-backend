from rest_framework import serializers

from api.models import Atividade





class AtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atividade
        fields = ['id','nome','descricao','dia_semana','gif_exercicio']