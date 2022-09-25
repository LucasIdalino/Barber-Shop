from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticatedOrReadOnly
from app.models import *
from app.serializers import *


class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    


class ClienteModelViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    

class ServicoViewSet(ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class AtendimentoViewset(ModelViewSet):
    '''Atendimentos'''
    queryset = Atendimento.objects.all()
    serializer_class = AtendimentoSerializer

