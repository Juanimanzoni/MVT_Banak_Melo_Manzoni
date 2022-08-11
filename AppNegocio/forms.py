from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClientesForm(forms.Form):
    #especifico campos
    nombre = forms.CharField(max_length=50)
    tipo = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=50)
    email = forms.EmailField()
    fecha_alta= forms.DateField(input_formats=['%d/%m/%Y'])
    
class ProveedoresForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=50)
    email = forms.EmailField()
    rubro = forms.CharField(max_length=50)
    fecha_alta= forms.DateField(input_formats=['%d/%m/%Y'])

class ArticulosForm(forms.Form):
    codigo_sku = forms.CharField(max_length=50)
    nombre= forms.CharField(max_length=50)
    familia= forms.CharField(max_length=50)
    stock= forms.IntegerField()
    costo= forms.FloatField()
    precio_venta= forms.FloatField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    first_name= forms.CharField(max_length=50)
    last_name= forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen= forms.ImageField(label="Imagen")