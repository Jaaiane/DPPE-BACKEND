# api/urls.py
from django.urls import path
from .views import ArtigoListCreate, ImagemListCreate, VideoListCreate

urlpatterns = [
    path('artigos/', ArtigoListCreate.as_view(), name='artigos'),
    path('imagens/', ImagemListCreate.as_view(), name='imagens'),
    path('videos/', VideoListCreate.as_view(), name='videos'),
]