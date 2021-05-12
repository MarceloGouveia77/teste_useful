from django.db import models
from empresa.models import Unidade
from django.conf import settings
# Create your models here.

class Motorista(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=50)
    unidade = models.ForeignKey(Unidade, related_name='Unidade', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Movimentacao(models.Model):
    motorista = models.ForeignKey(Motorista, related_name='Motorista', on_delete=models.CASCADE)
    origem = models.ForeignKey(Unidade, related_name='Unidade_Origem', on_delete=models.CASCADE)
    hora_saida = models.DateTimeField('Saida', auto_now_add=True)
    destino = models.ForeignKey(Unidade, related_name='Unidade_Destino', on_delete=models.CASCADE)
    hora_chegada = models.DateTimeField('Chegada', auto_now=True)
    concluido = models.BooleanField('Concluido', default=False)

    def __str__(self):
        return f'Origem: {self.origem} / Destino: {self.destino}'

    def obter_data_saida(self):
        return self.hora_saida.strftime('%d/%m/%Y')

    def obter_data_chegada(self):
        return self.hora_chegada.strftime('%d/%m/%Y')
