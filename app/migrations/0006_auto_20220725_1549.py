# Generated by Django 3.2.14 on 2022-07-25 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20220725_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='horario',
        ),
        migrations.RemoveField(
            model_name='atendimento',
            name='servico',
        ),
        migrations.AddField(
            model_name='atendimento',
            name='servico',
            field=models.ManyToManyField(related_name='serviços', to='app.Servico'),
        ),
    ]
