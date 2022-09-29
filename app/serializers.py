from asyncore import read
from app.models import *
from rest_framework import serializers
from rest_framework.serializers import ValidationError



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
        
        
    #TODO O método create não contém o parâmetro 'instance'. Neste método, deve ser verificado
    #se o funcionário escolhido contém a habilidade desejada pela o usuário.

    def create(self, validated_data, instance):
        funcionario = validated_data['funcionario']
        habilidade = validated_data['servico']
        query = Funcionario.objects.all()

        if validated_data['servico'] in instance.funcionario.habilidade:
            atendimento = Atendimento.objects.create(**validated_data)
            atendimento.save()
            return atendimento
        else:
            raise ValidationError(
                {'erro': f'O funcionário {funcionario} não tem está habilidade {habilidade}.'}
            )
