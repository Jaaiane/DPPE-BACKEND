from rest_framework import viewsets
from .models import Area, Pergunta, Resposta, Documento, DocumentoSolicitado, Agendamento
from .serializers import AreaSerializer, PerguntaSerializer, RespostaSerializer, DocumentoSerializer, DocumentoSolicitadoSerializer, AgendamentoSerializer

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class PerguntaViewSet(viewsets.ModelViewSet):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntaSerializer


class RespostaViewSet(viewsets.ModelViewSet):
    queryset = Resposta.objects.all()
    serializer_class = RespostaSerializer


class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer


class DocumentoSolicitadoViewSet(viewsets.ModelViewSet):
    queryset = DocumentoSolicitado.objects.all()
    serializer_class = DocumentoSolicitadoSerializer


class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer