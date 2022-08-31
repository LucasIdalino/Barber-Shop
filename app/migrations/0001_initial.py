# Generated by Django 3.2.14 on 2022-08-31 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('idade', models.DateField(auto_now=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Serviço',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servico', models.CharField(max_length=100)),
                ('preco', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('habilidade', models.ManyToManyField(to='app.Serviço')),
            ],
        ),
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.DateTimeField()),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.funcionario')),
                ('servico', models.ManyToManyField(to='app.Serviço')),
            ],
        ),
    ]
