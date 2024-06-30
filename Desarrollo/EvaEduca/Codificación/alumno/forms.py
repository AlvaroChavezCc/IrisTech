from django import forms
from .models import evaluacion



class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=100)
    contrasena = forms.CharField(widget=forms.PasswordInput())


class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = evaluacion
        fields = ['file', 'id_curso', 'id_alumno', 'id_tarea']
