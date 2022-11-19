from debug_toolbar import APP_NAME
from django.urls import path
from . import views

APP_NAME = 'Pedido'

urlpatterns = [
    path('', views.Pagar.as_view(), name='Pagar'),
    path('FecharPedido/', views.FecharPedido.as_view(), name='FecharPedido'),
    path('Detalhe/', views.Detalhe.as_view(), name='Detalhe'),



]
