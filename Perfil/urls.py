from debug_toolbar import APP_NAME
from django.urls import path
from . import views

APP_NAME = 'Perfil'

urlpatterns = [
    path('', views.Criar.as_view(), name='Criar'),
    path('Atualizar/', views.Atualizar.as_view(), name='Atualizar'),
    path('Login/', views.Login.as_view(), name='Login'),
    path('Logout/', views.Logout.as_view(), name='Logout'),

]
