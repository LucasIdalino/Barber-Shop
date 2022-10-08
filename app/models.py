from django.db import models
from django.db.models import F
from django.utils import timezone



class Servico(models.Model):
    servico = models.CharField(max_length=100, blank=False, null=False)
    preco = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return '%s' % (self.servico)


class Cliente(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    sobrenome = models.CharField(max_length=100, blank=False, null=False)
    nascimento = models.DateField(default=timezone.now())
    email = models.EmailField(blank=False, null=False)

    def __str__(self):
        return '%s' % (self.nome)


class Funcionario(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    habilidade = models.ManyToManyField(Servico)

    def __str__(self):
        return '%s' % (self.nome)


class Atendimento(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    servico = models.ManyToManyField(Servico)
    horario = models.DateTimeField()

    def __str__(self):
        return 'Seu atendimento foi agendado para %s' % (self.horario)

