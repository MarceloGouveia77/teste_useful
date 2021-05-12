# Generated by Django 3.2.2 on 2021-05-12 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('rua', models.CharField(max_length=50, verbose_name='Rua')),
                ('numero', models.CharField(max_length=50, verbose_name='Numero')),
                ('codigo_postal', models.CharField(max_length=50, verbose_name='Código Postal')),
            ],
        ),
    ]
