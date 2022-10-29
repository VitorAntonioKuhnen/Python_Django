from django.db import models
from django.contrib.auth.models import User #Importe para utilizar o ForeingKey

class Tarefas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #Informa que a tarefa está vinculada a um usuario, Para vincular troque o "User", o On_delite serve para deletar todos os relacionamentos juntamente 
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    datas = models.CharField(max_length=10)
    status = models.BooleanField()

    def __str__(self):
        return self.titulo