from django import forms
from .models import Recetas, Usuario

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Recetas
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

