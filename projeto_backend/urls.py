from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('biblioteca/v1/', include('biblioteca.urls')),  # Incluindo as URLs da API
    path('auth_app/', include('auth_app.urls')),
    path('agendamento/', include('agendamento.urls')),
    path('processos/', include('processos.urls')),
]