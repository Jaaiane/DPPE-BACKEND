from django.db import models

# Create your models here.

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

class Imagem(models.Model):
    titulo = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='imagens/')
    data_criacao = models.DateTimeField(auto_now_add=True)

class Video(models.Model):
    titulo = models.CharField(max_length=200)
    url = models.URLField()
    data_criacao = models.DateTimeField(auto_now_add=True)
