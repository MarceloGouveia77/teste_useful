from django.shortcuts import render, HttpResponse
from django.apps import apps

# Create your views here.

def index(request):

    return render(request, 'core/base.html', {})

def remover_registro(request, pk, app, model):
    if request.method == "POST":
        Model = apps.get_model(app, model)
        instance = Model.objects.get(id=pk)
        instance.delete()
        return HttpResponse('<script>window.location = document.referrer;</script>') # RETORNA PRA PÁGINA ANTERIOR
    return render(request, 'core/remover_registro.html', {'pk': pk, 'app': app, 'model': model})