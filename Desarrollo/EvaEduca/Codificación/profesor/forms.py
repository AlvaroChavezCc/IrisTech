from django import forms
from django.core.exceptions import ValidationError

from administrador.models import tareas
from alumno.models import evaluacion
from profesor.models import profesor

class ResetForm(forms.ModelForm):
    confirmar_contrasena = forms.CharField(widget=forms.PasswordInput(), required=False, label="Confirmar Contraseña")

    class Meta:
        model = profesor
        fields = ['usuario', 'contrasena']
        widgets = {
            'contrasena': forms.PasswordInput(),
        }
        labels = {
            'usuario': 'Usuario',
            'contrasena': 'Contraseña',
        }

    def clean(self):
        cleaned_data = super().clean()
        usuario = cleaned_data.get('usuario')
        contrasena = cleaned_data.get('contrasena')
        confirmar_contrasena = cleaned_data.get('confirmar_contrasena')

        # Si se proporciona una nueva contraseña, verificar su longitud y coincidencia con confirmar_contrasena
        if contrasena:
            if len(contrasena) < 6:
                self.add_error('contrasena', "La contraseña debe tener al menos 6 caracteres")
            if contrasena != confirmar_contrasena:
                self.add_error('confirmar_contrasena', "Las contraseñas no coinciden")
        
        # Si se cambia el usuario, la contraseña es obligatoria para confirmar la identidad
        if usuario and not contrasena:
            self.add_error('contrasena', "Debe proporcionar su contraseña para cambiar el usuario")

        return cleaned_data


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

class EvaluarManualmenteForm(forms.ModelForm):
    class Meta:
        model = evaluacion
        fields = ['nota', 'respuesta']
        labels = {
            'nota': 'Nota',
            'respuesta': 'Respuesta',
        }
        widgets = {
            'respuesta': forms.Textarea(attrs={'rows': 5}),
        }

    def clean_nota(self):
        nota = self.cleaned_data['nota']
        if nota < 0 or nota > 20:
            raise forms.ValidationError('La nota debe estar entre 0 y 20.')
        return nota
    
class JustificarNotaForm(forms.Form):
    respuesta = forms.CharField(widget=forms.Textarea, label='Justificación de la nota')

class ModificarNotaForm(forms.Form):
    nota = forms.DecimalField(max_digits=4, decimal_places=2, label='Nueva Nota')
    respuesta_evaluacion = forms.CharField(widget=forms.Textarea, label='Nueva Respuesta de Evaluación')
    respuesta_reclamo = forms.CharField(widget=forms.Textarea, label='Justificación de la Nota')