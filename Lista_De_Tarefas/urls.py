from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista, name='index'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('adicionar_item/', views.adicionar_item, name='adicionar_item'),
    path('deletar/<int:id>/', views.deletar, name='deletar'),
    path('altStatus/<int:id>/', views.altStatus, name='altStatus'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('buscar/', views.buscar, name='buscar'),
]