from django.urls import path
from empresa import views

app_name = 'empresa'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('unidades/', views.listar_unidades, name='listar_unidades')
]
