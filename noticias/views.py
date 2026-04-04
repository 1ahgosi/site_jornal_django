from django.shortcuts import render, get_object_or_404, redirect
from .models import Artigo, Comentario

def lista_artigos(request):
    artigos = Artigo.objects.all()
    return render(request, 'noticias/lista_artigos.html', {'artigos': artigos})

def detalhe_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    return render(request, 'noticias/detalhe_artigo.html', {'artigo': artigo})

# --- NOVA FUNÇÃO DA FASE 4 ---
def comentarios_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    
    # Se o utilizador submeteu o formulário (POST)
    if request.method == 'POST':
        # Vai buscar o texto que foi escrito no formulário HTML
        texto = request.POST.get('texto_comentario')
        
        # Se o texto não estiver vazio, cria e guarda o comentário
        if texto:
            Comentario.objects.create(artigo=artigo, texto_comentario=texto)
            # Recarrega a página para mostrar o novo comentário
            return redirect('comentarios_artigo', artigo_id=artigo.id)
    
    # Se for apenas para ver a página (GET)
    # Vai buscar todos os comentários ligados a este artigo específico
    comentarios = artigo.comentarios.all()
    
    return render(request, 'noticias/comentarios_artigo.html', {
        'artigo': artigo, 
        'comentarios': comentarios
    })