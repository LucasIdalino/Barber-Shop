# Generated by Django 3.2.14 on 2022-07-25 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20220725_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='atendimento',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.cliente'),
        ),
    ]