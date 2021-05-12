from django.conf.urls import url
from django.urls import path
from motorista import views

app_name = 'motorista'

urlpatterns = [
    path('', views.listar_motoristas, name='listar_motoristas'),
    path('cadastrar/', views.cadastrar_motorista, name='cadastrar_motorista'),
    path('detalhe/<int:pk>/', views.detalhe_motorista, name='detalhe_motorista'),
    path('editar/<int:pk>/', views.editar_motorista, name='editar_motorista')
]
