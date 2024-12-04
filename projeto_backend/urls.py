from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('biblioteca/v1/', include('biblioteca.urls')),  # Incluindo as URLs da API
    path('auth_app/', include('auth_app.urls')),
    path('agendamento/', include('agendamento.urls')),
    path('processos/', include('processos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)