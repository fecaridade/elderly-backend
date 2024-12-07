from django.shortcuts import render
from rest_framework.mixins import ListModelMixin

from api.models import Atividade
from api.serializers import AtividadeSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class AtividadeViewSet(ListModelMixin,viewsets.GenericViewSet):
    serializer_class = AtividadeSerializer
    queryset = Atividade.objects.all()

    @action(detail=False, methods=["get"], url_path="dias")
    def listar_dias(self, request):
        dias_com_atividades = Atividade.objects.values_list("dia_semana", flat=True).distinct()
        return Response(dias_com_atividades)

