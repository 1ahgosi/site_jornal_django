from django.db import models

class Artigo(models.Model):
    # Campo para o título (máximo de 200 caracteres é um padrão comum)
    titulo = models.CharField(max_length=200)
    # Campo para o conteúdo do artigo (sem limite de caracteres)
    corpo_texto = models.TextField()

    def __str__(self):
        # Isto faz com que o Django mostre o título do artigo no Admin
        return self.titulo

class Comentario(models.Model):
    # Relação ForeignKey: associa um comentário a um artigo específico.
    # on_delete=models.CASCADE significa que se o artigo for apagado, 
    # os comentários dele também serão.
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    # O conteúdo do comentário
    texto_comentario = models.TextField()

    def __str__(self):
        # Mostra uma breve descrição do comentário no Admin
        return f"Comentário em: {self.artigo.titulo}"