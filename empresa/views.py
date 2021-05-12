from django.contrib.auth.decorators import login_required
from core.decorators import admin_required
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from empresa.models import Unidade
from empresa.forms import UnidadeForm
from motorista.forms import MovimentacaoForm
from motorista.models import Motorista, Movimentacao

# Create your views here.
@login_required(login_url='/login')
@admin_required(login_url='/motorista/portal', redirect_field_name=None)
def dashboard(request):
    movimentacoes = Movimentacao.objects.all()

    return render(request, 'dashboard/index.html', {'movimentacoes': movimentacoes, 'dashboard_active': 'active'})

@login_required(login_url='/login')
@admin_required(login_url='/motorista/portal', redirect_field_name=None)
def listar_movimentacoes(request):
    movimentacoes = Movimentacao.objects.all()

    return render(request, 'movimentacao/index.html', {'movimentacoes': movimentacoes, 'movimentacoes_active': 'active'})

@login_required(login_url='/login')
@admin_required(login_url='/motorista/portal', redirect_field_name=None)
def cadastrar_movimentacao(request):
    form = MovimentacaoForm(request.POST or None, hidden=False)
    
    if form.is_valid():
        form.save()
        return HttpResponse('<script>window.location.reload()</script>')
    return render(request, 'movimentacao/cadastrar.html', {'form': form})

@login_required(login_url='/login')
@admin_required(login_url='/motorista/portal', redirect_field_name=None)
def listar_unidades(request):
    unidades = Unidade.objects.all()

    return render(request, 'unidade/index.html', {'unidades': unidades, 'unidades_active': 'active'})

@login_required(login_url='/login')
@admin_required(login_url='/motorista/portal', redirect_field_name=None)
def cadastrar_unidade(request):
    form = UnidadeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponse('<script>window.location.reload()</script>')
    return render(request, 'unidade/cadastrar.html', {'form': form})

@login_required(login_url='/login')
@admin_required(login_url='/motorista/portal', redirect_field_name=None)
def editar_unidade(request, pk):
    instance = Unidade.objects.get(id=pk)
    form = UnidadeForm(request.POST or None, instance=instance)

    if form.is_valid():
        form.save()
        return HttpResponse('<script>window.location.reload()</script>')
    return render(request, 'unidade/editar.html', {'form': form, 'pk': pk})

@login_required(login_url='/login')
@admin_required(login_url='/motorista/portal', redirect_field_name=None)
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

@login_required(login_url='/login')
@admin_required(login_url='/motorista/portal', redirect_field_name=None)
def gerar_relatorio(request):
    movimentacoes = Movimentacao.objects.all()
    motoristas = Motorista.objects.all()
    unidades = Unidade.objects.all()

    context = {
        'motoristas': motoristas,
        'unidades': unidades
    }

    if request.method == "GET":
        id_origem = request.GET.get('id_origem')
        id_destino = request.GET.get('id_destino')
        id_motorista = request.GET.get('id_motorista')

    if request.GET.get('gerar'):
        origem_str = "Todos" if id_origem == '0' else unidades.get(id=id_origem)
        movimentacoes = movimentacoes.filter(origem=origem_str) if origem_str != "Todos" else movimentacoes

        destino_str = "Todos" if id_destino == '0' else unidades.get(id=id_destino)
        movimentacoes = movimentacoes.filter(destino=destino_str) if destino_str != "Todos" else movimentacoes

        motorista_str = "Todos" if id_motorista == '0' else motoristas.get(id=id_motorista)
        movimentacoes = movimentacoes.filter(motorista=motorista_str) if motorista_str != "Todos" else movimentacoes

        context = {
            'origem_str': origem_str,
            'destino_str': destino_str,
            'motorista_str': motorista_str,
            'movimentacoes': movimentacoes
        }
        return render(request, 'movimentacao/relatorio.html', context)
    return render(request, 'movimentacao/gerar_relatorio.html', context)

