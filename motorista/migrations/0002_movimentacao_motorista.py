# Generated by Django 3.2.2 on 2021-05-12 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motorista', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimentacao',
            name='motorista',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Motorista', to='motorista.motorista'),
            preserve_default=False,
        ),
    ]
