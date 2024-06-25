from django import forms
from django.core.exceptions import ValidationError

from administrador.models import tareas
from profesor.models import profesor

class ResetForm(forms.ModelForm):
    class Meta:
        model = profesor
        fields = ['usuario', 'contrasena']
        widgets = {
            'contrasena': forms.PasswordInput(),
        }

    def clean_contrasena(self):
        contrasena = self.cleaned_data.get('contrasena')
        if len(contrasena) < 6:
            raise forms.ValidationError("La contraseña debe tener al menos 6 caracteres")
        return contrasena

class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=50, label='Usuario')
    contrasena = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

class crear_task(forms.Form):
    tema = forms.CharField(label="Asunto", max_length=100)
    descripcion = forms.CharField(label="Descripcion", widget=forms.Textarea)
    rubrica = forms.FileField(label="Rúbrica", required=False, widget=forms.FileInput)
    archivo = forms.FileField(label="Archivo", required=False, widget=forms.FileInput)
    
    def clean_rubrica(self):
        rubrica = self.cleaned_data.get('rubrica')
        if rubrica:
            if not rubrica.name.endswith('.docx'):
                raise ValidationError('El archivo de la rúbrica debe estar en formato .docx')
        return rubrica

    def clean_archivo(self):
        archivo = self.cleaned_data.get('archivo')
        if archivo:
            if not archivo.name.endswith('.docx'):
                raise ValidationError('El archivo debe estar en formato .docx')
        return archivo

class EditarTareaForm(forms.ModelForm):
    class Meta:
        model = tareas
        fields = ['tema', 'descripcion', 'rubrica', 'archivo']