from socket import fromshare
from django import forms

class ClientesForm(forms.Form):
    #especifico campos
    nombre = forms.CharField(max_length=50)
    tipo = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=50)
    email = forms.EmailField()
    fecha_alta= forms.DateField()
    
class ProveedoresForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=50)
    email = forms.EmailField()
    rubro = forms.CharField(max_length=50)
    fecha_alta= forms.DateField()

class ArticulosForm(forms.Form):
    codigo_sku = forms.CharField(max_length=50)
    nombre= forms.CharField(max_length=50)
    familia= forms.CharField(max_length=50)
    stock= forms.IntegerField()
    costo= forms.FloatField()
    precio_venta= forms.FloatField()