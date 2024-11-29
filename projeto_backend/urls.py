from django.urls import path, re_path
from auth_app import views as auth
from biblioteca import views as bibli


urlpatterns = [
    re_path('login', auth.login),
    re_path('signup', auth.signup),
    re_path('test_token', auth.test_token),
    re_path('test_biblioteca', bibli.ola),
]