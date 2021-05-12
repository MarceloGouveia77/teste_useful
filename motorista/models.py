from django.db import models
from empresa.models import Unidade
# Create your models here.

class Motorista(models.Model):
    nome = models.CharField('Nome', max_length=50)
    unidade = models.ForeignKey(Unidade, related_name='Unidade', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Movimentacao(models.Model):
    origem = models.ForeignKey(Unidade, related_name='Unidade_Origem', on_delete=models.CASCADE)
    hora_saida = models.DateTimeField('Saida', auto_now_add=True)
    destino = models.ForeignKey(Unidade, related_name='Unidade_Destino', on_delete=models.CASCADE)
    hora_chegada = models.DateTimeField('Chegada', auto_now=True)

    def __str__(self):
        return f'Origem: {self.origem} / Destino: {self.destino}'