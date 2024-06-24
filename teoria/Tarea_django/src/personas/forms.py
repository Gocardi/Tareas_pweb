from django import forms

class PersonaForm(forn.Form):
    nombre = forms.Charfield(max_length=100)
    edad = forms.IntegerField()
    email = forms.EmailField()
