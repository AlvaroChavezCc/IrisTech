from django import forms

class UploadRubricaForm(forms.Form):
    file = forms.FileField()
