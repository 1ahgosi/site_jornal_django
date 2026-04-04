from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto_comentario']
        # Aqui injetamos as classes do Bootstrap diretamente pelo Python!
        widgets = {
            'texto_comentario': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4, 
                'placeholder': 'Deixa aqui a tua opinião...'
            }),
        }