from django.shortcuts import render
from motorista.models import Motorista, Movimentacao

# Create your views here.
def listar_motoristas(request):
    motoristas = Motorista.objects.all()

    return render(request, 'motorista/index.html', {'motoristas': motoristas})