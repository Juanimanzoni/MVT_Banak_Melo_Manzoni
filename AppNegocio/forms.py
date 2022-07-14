from socket import fromshare
from django import forms

class ClientesForm(forms.Form):
    #especifico campos
    nombre_cli = forms.CharField(max_length=50)
    tipo_cli = forms.CharField(max_length=50)
    direccion_cli = forms.CharField(max_length=50)
    email_cli = forms.EmailField()
    fecha_alta_cli= forms.DateField()
    
class ProveedoresForm(forms.Form):
    nombre_prov = forms.CharField(max_length=50)
    direccion_prov = forms.CharField(max_length=50)
    email_prov = forms.EmailField()
    rubro_prov = forms.CharField(max_length=50)
    fecha_alta_prov= forms.DateField()

class ArticulosForm(forms.Form):
    codigo_sku_art = forms.CharField(max_length=50)
    nombre_art= forms.CharField(max_length=50)
    familia_art= forms.CharField(max_length=50)
    stock_art= forms.IntegerField()
    costo_art= forms.FloatField()
    precio_venta_art= forms.FloatField()