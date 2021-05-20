from django import forms
from django.forms import ModelForm
from .models import Contacto, Comentario


class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
        opcoes = [
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5)
        ]
        widgets = {
            'clareza': forms.RadioSelect(choices=opcoes),
            'rigor': forms.RadioSelect(choices=opcoes),
            'precisao': forms.RadioSelect(choices=opcoes),
        }
