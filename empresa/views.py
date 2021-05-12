from django.shortcuts import render
from empresa.models import Unidade

# Create your views here.

def dashboard(request):

    return render(request, 'dashboard/index.html', {})

def listar_unidades(request):
    unidades = Unidade.objects.all()

    return render(request, 'unidade/index.html', {'unidades': unidades})