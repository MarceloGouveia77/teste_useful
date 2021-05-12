from django.shortcuts import render, HttpResponse
from motorista.models import Motorista, Movimentacao
from motorista.forms import MotoristaForm, MovimentacaoForm
import datetime

# Create your views here.
def listar_motoristas(request):
    motoristas = Motorista.objects.all()

    return render(request, 'motorista/index.html', {'motoristas': motoristas, 'motoristas_active': 'active'})

def cadastrar_motorista(request):
    form = MotoristaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponse('<script>window.location.reload()</script>')
    return render(request, 'motorista/cadastrar.html', {'form': form})

def editar_motorista(request, pk):
    instance = Motorista.objects.get(id=pk)
    form = MotoristaForm(request.POST or None, instance=instance)

    if form.is_valid():
        form.save()
        return HttpResponse('<script>window.location.reload()</script>')
    return render(request, 'motorista/editar.html', {'form': form, 'pk':pk})

def cadastrar_movimentacao(request):
    motorista = Motorista.objects.get(usuario=request.user)
    inicial = {'motorista': motorista}

    form = MovimentacaoForm(request.POST or None, initial=inicial, hidden=True)
    
    if form.is_valid():
        form.save()
        return HttpResponse('<script>window.location.reload()</script>')
    return render(request, 'portal/movimentacao/cadastrar.html', {'form': form})

def confirmar_movimentacao(request, pk):
    movimentacao = Movimentacao.objects.get(id=pk, motorista__usuario=request.user)

    if request.method == "POST":
        movimentacao.concluido = True
        movimentacao.hora_chegada = datetime.datetime.now()
        movimentacao.save()
        return HttpResponse('<script>window.location.reload()</script>')
    return render(request, 'portal/movimentacao/confirmar.html', {'pk': pk})

def detalhe_motorista(request, pk):
    motorista = Motorista.objects.get(id=pk)
    movimentacoes = Movimentacao.objects.filter(motorista=motorista)

    context = {
        'motorista': motorista,
        'movimentacoes': movimentacoes,
        'motoristas_active': 'active'
    }

    return render(request, 'motorista/detalhe.html', context)

def portal_motorista(request):
    motorista = Motorista.objects.get(usuario=request.user)
    movimentacoes = Movimentacao.objects.filter(motorista=motorista)

    context = {
        'motorista': motorista,
        'qtd_movimentacoes': movimentacoes.count(),
        'movimentacoes': movimentacoes,
        'movimentacoes_aberto': movimentacoes.filter(concluido=False)
    }

    return render(request, 'portal/index.html', context)