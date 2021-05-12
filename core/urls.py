from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('remover_registro/<int:pk>/<str:app>/<str:model>/', views.remover_registro, name='remover_registro')
]