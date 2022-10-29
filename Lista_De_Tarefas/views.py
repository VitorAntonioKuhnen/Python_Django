from django.shortcuts import render, redirect
from .models import Tarefas
from django.contrib import auth
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='logar')
def lista(request):

    if request.user.is_superuser:
        tarefas = Tarefas.objects.all() #Permissão para que os super usuarios possam verificar mais de um item
        return render(request, 'listas.html', {'tarefas':tarefas})
    else:
        tarefas = Tarefas.objects.filter(usuario_id=request.user.id) #Filtro para trazer apenas a lista pertencente ao usuario logado
        return render(request, 'listas.html', {'tarefas':tarefas})

@login_required(redirect_field_name='logar')
def adicionar(request):
    return render(request, 'cadLista.html')

@login_required(redirect_field_name='logar')
def adicionar_item(request):
    titulo = request.POST.get('titulo')
    descricao = request.POST.get('descricao')
    datas = request.POST.get('datas')
    status = request.POST.get('status')

    if status == 'pendente':  #Pega pelo campo "Value="pendente"" e não pelo nome do item 
        status = True
    else:
        status = False
    
    Tarefas.objects.create(usuario_id=request.user.id, titulo=titulo, descricao=descricao, datas=datas, status=status) # foi necessario adicionar o usuario_id=request.user.id para cadastrar que o usuario atual é o dono desta lista 
    
    return redirect('index')

@login_required(redirect_field_name='logar')
def deletar(request, id):
    Tarefas.objects.get(id=id).delete()
    return redirect('index')

@login_required(redirect_field_name='logar')
def altStatus(request, id):
    tf = Tarefas.objects.get(id=id)
    tf.status = True
    tf.save()   
    return redirect('index')

@login_required(redirect_field_name='logar')
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

def buscar(request):
    termo = request.GET.get('termo')

    tarefas = Tarefas.objects.filter(titulo__icontains=termo)
    return render(request, 'listas.html', {'tarefas':tarefas})        