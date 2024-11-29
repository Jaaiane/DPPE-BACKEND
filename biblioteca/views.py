# from django.shortcuts import render

# Create your views here.
# api/views.py
from django.http import JsonResponse

def ola(request):
    return JsonResponse({"message": "Oi"})
