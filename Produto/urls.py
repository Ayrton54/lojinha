from django import views
from django.urls import path
from . import views

app_name = 'Produto'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name="lista"),
    path('<slug>', views.DetalheProdutos.as_view(), name="Detalhe"),
    path('AdicionarAoCarrinho/', views.AdicionarAoCarrinho.as_view(),
         name="AdicionarAoCarrinho"),
    path('RemoverDocarrinho/', views.RemoverDocarrinho.as_view(),
         name="RemoverDocarrinho"),
    path('Carrinho/', views.Carrinho.as_view(), name="Carrinho"),
    path('Finalizar/', views.Finalizar.as_view(), name="Finalizar"),


]
