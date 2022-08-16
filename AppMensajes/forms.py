from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MensajeGlobalForm(forms.Form):
    
    texto_msg = forms.CharField(widget=forms.Textarea, label='Mensaje')
    imagen_msg = forms.ImageField(label="Imagen")
    