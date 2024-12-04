# processos/urls.py
from django.urls import path
from .views import ProcessoList

urlpatterns = [
    path('processos/', ProcessoList.as_view(), name='processos'),
]