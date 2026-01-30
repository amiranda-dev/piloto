from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('sobre/', views.sobre, name='sobre'),
    path('ajuda/', views.ajuda, name='ajuda'),
    path('item/<int:id>/', views.item, name='item'),
    path('perfil/<str:usuario>/', views.perfil, name='perfil'),
    
    # Rota do exercício de Dia da Semana
    path('diasemana/<int:dia>/', views.dia_semana, name='diasemana'),
    
    # Rota para evitar o erro do link "Produtos"
    path('produtos/', views.produto, name='produto'), 
]