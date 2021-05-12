from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from empresa.models import Unidade
from empresa.forms import UnidadeForm
from motorista.models import Motorista, Movimentacao

# Create your views here.

def dashboard(request):
    movimentacoes = Movimentacao.objects.all()

    return render(request, 'dashboard/index.html', {'movimentacoes': movimentacoes, 'dashboard_active': 'active'})

def listar_unidades(request):
    unidades = Unidade.objects.all()

    return render(request, 'unidade/index.html', {'unidades': unidades, 'unidades_active': 'active'})

def cadastrar_unidade(request):
    form = UnidadeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponse('<script>window.location.reload()</script>')
    return render(request, 'unidade/cadastrar.html', {'form': form})

def detalhe_unidade(request, pk):
    unidade = Unidade.objects.get(id=pk)
    movimentacoes_origem = Movimentacao.objects.filter(origem=unidade)
    movimentacoes_destino = Movimentacao.objects.filter(destino=unidade)

    context = {
        'unidade': unidade,
        'movimentacoes_origem': movimentacoes_origem,
        'movimentacoes_destino': movimentacoes_destino,
        'total_motoristas': Motorista.objects.filter(unidade=unidade).count(),
        'unidades_active': 'active'
    }

    return render(request, 'unidade/detalhe.html', context)