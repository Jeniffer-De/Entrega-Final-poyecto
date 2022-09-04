from django import forms

class Formulario_datos(forms.Form):
    nombre = forms.CharField(max_length=50)
    Cedula = forms.FloatField()
    cargo =  forms.CharField(max_length=50)
    Fecha_inicio = forms.FloatField()
    Salario = forms.FloatField()
    Tipo_de_contrato = forms.CharField(max_length=50)