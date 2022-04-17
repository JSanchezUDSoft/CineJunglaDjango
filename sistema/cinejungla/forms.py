from django import forms
from .models import Multiplex, Usuario, Sala

class RegistrarMultiplexForm(forms.ModelForm):
    class Meta:
        model = Multiplex
        fields = '__all__'

class RegistrarSalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = '__all__'

class RegistrarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'