from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Artigo, Imagem, Video
from .serializers import ArtigoSerializer, ImagemSerializer, VideoSerializer

class ArtigoListCreate(generics.ListCreateAPIView):
    queryset = Artigo.objects.all()
    serializer_class = ArtigoSerializer

class ImagemListCreate(generics.ListCreateAPIView):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer

class VideoListCreate(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer