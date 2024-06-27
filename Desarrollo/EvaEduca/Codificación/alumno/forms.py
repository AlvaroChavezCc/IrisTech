from django import forms
from .models import Respuesta


class SubirRespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ['archivo_respuesta']  # Asegúrate de usar el nombre correcto del campo

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=100)
    contrasena = forms.CharField(widget=forms.PasswordInput())
