from django.db import models

class Tarefas(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    datas = models.DateField()
    status = models.BooleanField()

    def __str__(self):
        return self.titulo