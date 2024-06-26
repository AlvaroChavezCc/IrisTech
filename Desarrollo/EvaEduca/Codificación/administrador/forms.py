from django import forms
from .models import curso
from profesor.models import profesor

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = profesor
        fields = ['nombre', 'correo', 'usuario', 'contrasena', 'id_inst_ed']

class CursoForm(forms.ModelForm):
    class Meta:
        model = curso
        fields = ['nombre', 'descripcion', 'id_profesor', 'id_inst_ed']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
