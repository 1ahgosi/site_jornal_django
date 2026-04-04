from django.urls import path
from . import views

urlpatterns = [
    # Rota para a página inicial (lista de artigos)
    path('', views.lista_artigos, name='lista_artigos'),
    # Rota para o detalhe de um artigo específico
    path('artigo/<int:artigo_id>/', views.detalhe_artigo, name='detalhe_artigo'),
]