from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages # Importante para os alertas
from .models import Artigo, Comentario
from .forms import ComentarioForm # Importamos o nosso novo formulário

# (As views lista_artigos e detalhe_artigo continuam iguais, não as apagues!)
def lista_artigos(request):
    artigos = Artigo.objects.all()
    return render(request, 'noticias/lista_artigos.html', {'artigos': artigos})

def detalhe_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    return render(request, 'noticias/detalhe_artigo.html', {'artigo': artigo})

def comentarios_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    comentarios = artigo.comentarios.all()
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST) # Passamos os dados para o Form do Django
        if form.is_valid(): # O Django valida se é seguro e está correto
            novo_comentario = form.save(commit=False)
            novo_comentario.artigo = artigo
            novo_comentario.save()
            
            # Cria a mensagem de sucesso
            messages.success(request, 'O teu comentário foi publicado com sucesso!')
            return redirect('comentarios_artigo', artigo_id=artigo.id)
    else:
        form = ComentarioForm() # Cria um formulário vazio
        
    return render(request, 'noticias/comentarios_artigo.html', {
        'artigo': artigo, 
        'comentarios': comentarios,
        'form': form # Enviamos o formulário para o template
    })