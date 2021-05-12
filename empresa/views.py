from django.shortcuts import render
from empresa.models import Unidade
from motorista.models import Movimentacao

# Create your views here.

def dashboard(request):
    movimentacoes = Movimentacao.objects.all()

    return render(request, 'dashboard/index.html', {'movimentacoes': movimentacoes, 'dashboard_active': 'active'})

def listar_unidades(request):
    unidades = Unidade.objects.all()

    return render(request, 'unidade/index.html', {'unidades': unidades, 'unidades_active': 'active'})