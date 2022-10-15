from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista, name='index'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('adicionar_item/', views.adicionar_item, name='adicionar_item'),
]