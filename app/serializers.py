from asyncore import read
from app.models import *
from rest_framework import serializers



class FuncionarioSerializer(serializers.ModelSerializer):
    habilidade = serializers.SlugRelatedField(
        many = True,
        queryset=Servico.objects.all(),
        slug_field = 'servico'
    )

    class Meta:
        model = Funcionario
        fields = ('nome', 'habilidade')
        

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'
    

class AtendimentoSerializer(serializers.ModelSerializer):
    servico = serializers.SlugRelatedField(
        many=True,
        queryset=Servico.objects.all(),
        slug_field='servico'
    )

    class Meta:
        model = Atendimento
        fields = '__all__'    
        
