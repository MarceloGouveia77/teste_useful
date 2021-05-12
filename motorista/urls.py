from django.conf.urls import url
from django.urls import path
from motorista import views

app_name = 'motorista'

urlpatterns = [
    path('', views.listar_motoristas, name='listar_motoristas'),
]
