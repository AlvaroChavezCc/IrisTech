from django import forms
from .models import evaluacion
from administrador.models import curso, tareas

class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=100)
    contrasena = forms.CharField(widget=forms.PasswordInput())

class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = evaluacion
        fields = ['file', 'id_curso', 'id_tarea']

    def __init__(self, *args, **kwargs):
        alumno = kwargs.pop('alumno', None)
        curso_id = kwargs.pop('curso_id', None)
        super(EvaluacionForm, self).__init__(*args, **kwargs)

        if alumno:
            self.fields['id_curso'].queryset = curso.objects.filter(id=alumno.id_curso_id)
            self.fields['id_curso'].label_from_instance = lambda obj: obj.nombre

        if curso_id:
            self.fields['id_tarea'].queryset = tareas.objects.filter(id_curso_id=curso_id)
            self.fields['id_tarea'].label_from_instance = lambda obj: obj.tema
            self.fields['id_tarea'].disabled = False
        else:
            self.fields['id_tarea'].queryset = tareas.objects.none()
            self.fields['id_tarea'].disabled = True
