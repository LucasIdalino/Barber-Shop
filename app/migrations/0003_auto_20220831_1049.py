# Generated by Django 3.2.14 on 2022-08-31 13:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_serviço_servico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='idade',
        ),
        migrations.AddField(
            model_name='cliente',
            name='nascimento',
            field=models.DateField(default=datetime.datetime(2022, 8, 31, 10, 49, 32, 151808)),
        ),
    ]
