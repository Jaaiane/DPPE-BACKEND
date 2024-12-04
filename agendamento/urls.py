# api/urls.py
from django.urls import path
from .views import AreaViewSet, PerguntaViewSet, RespostaViewSet, DocumentoViewSet, DocumentoSolicitadoViewSet, AgendamentoViewSet

urlpatterns = [
    path('areas/', AreaViewSet.as_view({'get': 'list', 'post': 'create'}), name='areas'),
    path('perguntas/', PerguntaViewSet.as_view({'get': 'list', 'post': 'create'}), name='perguntas'),
    path('respostas/', RespostaViewSet.as_view({'get': 'list', 'post': 'create'}), name='respostas'),
    path('documentos/', DocumentoViewSet.as_view({'get': 'list', 'post': 'create'}), name='documentos'),
    path('documentos-solicitados/', DocumentoSolicitadoViewSet.as_view({'get': 'list', 'post': 'create'}), name='documentos_solicitados'),
    path('agendamentos/', AgendamentoViewSet.as_view({'get': 'list', 'post': 'create'}), name='agendamentos'),
]