from django.db import models
from django.utils import timezone

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    corpo_texto = models.TextField()
    # Adicionamos a data de publicação (assume o momento em que é criado)
    data_publicacao = models.DateTimeField(default=timezone.now)

    class Meta:
        # Ordena os artigos do mais recente para o mais antigo (o sinal '-' faz a inversão)
        ordering = ['-data_publicacao']

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    texto_comentario = models.TextField(verbose_name="Escreva aqui a sua opinião")
    # Guarda automaticamente o momento exato em que o comentário foi feito
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_criacao']

    def __str__(self):
        return f"Comentário em: {self.artigo.titulo}"