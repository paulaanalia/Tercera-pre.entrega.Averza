from django import forms


class DiscoForms(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    anio = forms.IntegerField(required=True)