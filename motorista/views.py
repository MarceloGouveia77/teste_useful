from django.shortcuts import render, HttpResponse
from motorista.models import Motorista, Movimentacao
from motorista.forms import MotoristaForm

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

def detalhe_motorista(request, pk):
    motorista = Motorista.objects.get(id=pk)
    movimentacoes = Movimentacao.objects.filter(motorista=motorista)

    context = {
        'motorista': motorista,
        'movimentacoes': movimentacoes,
        'motoristas_active': 'active'
    }

    return render(request, 'motorista/detalhe.html', context)