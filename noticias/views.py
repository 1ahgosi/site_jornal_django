from django.shortcuts import render, get_object_or_404
from .models import Artigo

def lista_artigos(request):
    # Vai buscar todos os artigos à base de dados
    artigos = Artigo.objects.all()
    # Envia os artigos para o template 'lista_artigos.html'
    return render(request, 'noticias/lista_artigos.html', {'artigos': artigos})

def detalhe_artigo(request, artigo_id):
    # Vai buscar o artigo específico pelo ID ou devolve um erro 404 se não existir
    artigo = get_object_or_404(Artigo, id=artigo_id)
    # Envia o artigo para o template 'detalhe_artigo.html'
    return render(request, 'noticias/detalhe_artigo.html', {'artigo': artigo})