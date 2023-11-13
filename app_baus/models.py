from django.db import models

class Voluntarios(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    telefone = models.TextField(max_length=24)
    email = models.TextField(max_length=255)
    mensagem = models.TextField(max_length=600)
    data_cadastro = models.DateTimeField(auto_now_add=True)

class Admins(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    senha = models.TextField(max_length=128)
    token = models.TextField(max_length=128)
