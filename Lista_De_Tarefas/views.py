from django.shortcuts import render, redirect
from .models import Tarefas
from django.contrib import auth

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

    if status == 'pendente':  #Pega pelo campo "Value="pendente"" e não pelo nome do item 
        status = True
    else:
        status = False
    
    Tarefas.objects.create(titulo=titulo, descricao=descricao, datas=datas, status=status)
    
    return redirect('index')

def deletar(request, id):
    Tarefas.objects.get(id=id).delete()
    return redirect('index')


def altStatus(request, id):
    tf = Tarefas.objects.get(id=id)
    tf.status = True
    tf.save()   
    return redirect('index')


def editar(request, id):

    item = Tarefas.objects.get(id=id)
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        datas = request.POST.get('datas')
        status = request.POST.get('status')

        item.titulo = titulo
        item.descricao = descricao
        item.datas = datas

        if status == 'pendente':  #Pega pelo campo "Value="pendente"" e não pelo nome do item 
            status = True
        else:
            status = False
        item.status = status

        item.save()
        return redirect('index')
    else:       
        return render(request, 'altLista.html', {'item':item})


def logar(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        check = auth.authenticate(request, username=usuario, password=senha)
        
        if check is not None:
            auth.login(request, check)
            print(check)
            return redirect('index')
        else:
            return redirect('logar')
    else:        
        return render(request, 'login.html')