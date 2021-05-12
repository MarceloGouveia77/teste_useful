from django.urls import path
from empresa import views

app_name = 'empresa'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('unidades/', views.listar_unidades, name='listar_unidades'),
    path('unidades/cadastrar', views.cadastrar_unidade, name='cadastrar_unidade'),
    path('unidades/detalhe/<int:pk>/', views.detalhe_unidade, name='detalhe_unidade')
]
