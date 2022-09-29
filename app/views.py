from urllib import request
from app.models import *
from app.serializers import *
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly



class FuncionarioGenericsList(generics.ListCreateAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    

class FuncionarioGenericsRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class ClienteGenericsList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    

class ClienteGenericsRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class ServicoGenericsList(generics.ListCreateAPIView):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    

class ServicoGenericsRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class AtendimentoGenericsList(generics.ListCreateAPIView):
    '''Atendimentos'''
    queryset = Atendimento.objects.all()
    serializer_class = AtendimentoSerializer


class AtendimentoGenericsRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Atendimento.objects.all()
    serializer_class = AtendimentoSerializer

    