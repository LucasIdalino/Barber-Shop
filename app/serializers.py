from app.models import *
from datetime import date
from rest_framework.serializers import ModelSerializer


class FuncionarioSerializer(ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'
        depth = 1


class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        

class ServicoSerializer(ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'
        


class AtendimentoSerializer(ModelSerializer):
    class Meta:
        model = Atendimento
        fields = '__all__'      
        depth = 0
