from django.db import models


class Servico(models.Model):

    servico = models.CharField(max_length=50)
    preco = models.FloatField()

    def __str__(self):
        return self.servico


class Funcionario(models.Model):

    nome = models.CharField(max_length=100)
    habilidade = models.ManyToManyField(Servico)
    

    def __str__(self):
        return self.nome



class Cliente(models.Model):

    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome



class Atendimento(models.Model):

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    funcionario  = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    servico = models.ManyToManyField(Servico, related_name='serviços')
    horario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s foi atendido por %s' % (self.cliente, self.funcionario)