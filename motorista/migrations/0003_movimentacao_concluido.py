# Generated by Django 3.2.2 on 2021-05-12 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorista', '0002_movimentacao_motorista'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimentacao',
            name='concluido',
            field=models.BooleanField(default=False, verbose_name='Concluido'),
        ),
    ]
