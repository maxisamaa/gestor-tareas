from django import forms

class TareaForm(forms.Form):
    titulo = forms.CharField(max_length=200, label='Título')
    descripcion = forms.CharField(widget=forms.Textarea, required=False, label='Descripción')
