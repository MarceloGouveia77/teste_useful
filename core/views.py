from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from core.decorators import admin_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, HttpResponse
from django.apps import apps
from motorista.models import Motorista

# Create your views here.

def index(request):

    return redirect('empresa:dashboard')

@login_required(login_url='/login')
@admin_required(login_url='/motorista/portal', redirect_field_name=None)
def remover_registro(request, pk, app, model):
    if request.method == "POST":
        Model = apps.get_model(app, model)
        instance = Model.objects.get(id=pk)
        instance.delete()
        return HttpResponse('<script>window.location = document.referrer;</script>') # RETORNA PRA PÁGINA ANTERIOR
    return render(request, 'core/remover_registro.html', {'pk': pk, 'app': app, 'model': model})

def login_sistema(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)

        if usuario is not None:
            login(request, usuario)

            if usuario.is_superuser:
                return redirect('empresa:dashboard')
            else:
                try:
                    Motorista.objects.get(usuario=usuario) # VERIFICA SE O USUÁRIO TEM UM CADASTRO DE MOTORISTA VINCULADO
                    return redirect('motorista:portal_motorista')
                except Motorista.DoesNotExist:
                    return HttpResponse('<script>alert("Não há motorista vinculado com este usuário"); window.location = document.referrer;</script>')

    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form} )

@login_required(login_url='/login')
def logout_sistema(request):
    logout(request)
    return redirect('core:login_sistema')