from django import forms
from .models import evaluacion, curso, tareas

class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=100)
    contrasena = forms.CharField(widget=forms.PasswordInput())

class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = evaluacion
        fields = ['file', 'id_curso', 'id_tarea']

    def __init__(self, *args, **kwargs):
        alumno = kwargs.pop('alumno', None)
        super(EvaluacionForm, self).__init__(*args, **kwargs)
        
        if alumno:
            self.fields['id_curso'].queryset = curso.objects.filter(id=alumno.id_curso_id)
            self.fields['id_tarea'].queryset = tareas.objects.filter(id_curso=alumno.id_curso_id)
