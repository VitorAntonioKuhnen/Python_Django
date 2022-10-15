from django.shortcuts import render, redirect
from .models import Tarefas

def lista(request):
    tarefas = Tarefas.objects.all()
    return render(request, 'listas.html', {'tarefas':tarefas})

def adicionar(request):
    return render(request, 'cadLista.html')

def adicionar_item(request):
    titulo = request.POST.get('titulo')
    descricao = request.POST.get('descricao')
    datas = request.POST.get('datas')
    status = request.POST.get('status')

    if status == 'Pendente':
        status = False
    else:
        status = True

    Tarefas.objects.create(titulo=titulo, descricao=descricao, datas=datas, status=status)
    
    return redirect('index')