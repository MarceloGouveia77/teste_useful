from django.db import models

# Create your models here.
class Unidade(models.Model):
    nome = models.CharField('Nome', max_length=100, blank=False)
    cidade = models.CharField('Cidade', max_length=50)
    rua = models.CharField('Rua', max_length=50)
    numero = models.CharField('Numero', max_length=50)
    codigo_postal = models.CharField('Código Postal', max_length=50)

    def __str__(self):
        return self.nome