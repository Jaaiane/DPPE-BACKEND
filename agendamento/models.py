from django.db import models
from auth_app.models import Usuario  # Importando o modelo User do Django

class Area(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Pergunta(models.Model):
    area = models.ForeignKey(Area, related_name='perguntas', on_delete=models.CASCADE)
    texto = models.CharField(max_length=255)

    def __str__(self):
        return self.texto


class Agendamento(models.Model):
    area = models.ForeignKey(Area, related_name='agendamentos', on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, related_name='agendamentos', on_delete=models.CASCADE)  # Correção para ser ForeignKey
    data_hora = models.DateTimeField()
    descricao_caso = models.TextField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f'Agendamento {self.id} para {self.area}'


class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, related_name='respostas', on_delete=models.CASCADE)
    agendamento = models.ForeignKey(Agendamento, related_name='respostas', on_delete=models.CASCADE)
    texto = models.TextField()

    def __str__(self):
        return f'Resposta para {self.pergunta}'


class DocumentoSolicitado(models.Model):
    area = models.ForeignKey(Area, related_name='documentos_solicitados', on_delete=models.CASCADE)
    tipo_documento = models.CharField(max_length=255)

    def __str__(self):
        return self.tipo_documento


class Documento(models.Model):
    usuario = models.ForeignKey(Usuario, related_name='documentos', on_delete=models.CASCADE)  # Correção para ser ForeignKey
    agendamento = models.ForeignKey(Agendamento, related_name='documentos', on_delete=models.CASCADE)
    documento_solicitado = models.ForeignKey(DocumentoSolicitado, related_name='documentos', on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='documentos/')

    def __str__(self):
        return f'Documento {self.id} para o usuário {self.usuario.username}'