from django.contrib import admin
from .models import Artigo, Comentario

@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao') # Colunas visíveis na lista
    search_fields = ('titulo', 'corpo_texto')    # Adiciona uma barra de pesquisa

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('artigo', 'data_criacao', 'texto_comentario')
    list_filter = ('data_criacao', 'artigo')     # Adiciona filtros laterais