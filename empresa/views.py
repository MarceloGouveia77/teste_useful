from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from empresa.models import Unidade
from empresa.forms import UnidadeForm
from motorista.models import Movimentacao

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