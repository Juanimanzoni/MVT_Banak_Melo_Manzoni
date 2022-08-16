from ast import Return
from this import d
from django import http
from django.shortcuts import render
from AppNegocio.models import *
from AppMensajes.models import *
from django.http import HttpResponse
from AppMensajes.forms import *
import datetime
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import date
from django.db.models import Q


# Create your views here.
@ login_required
def mensajeGlobalFormulario(request):
    if request.method =='POST':
        form=MensajeGlobalForm(request.POST, request.FILES)
        if form.is_valid():
            info=form.cleaned_data
            texto_msg=info["texto_msg"]
            imagen_msg=info["imagen_msg"]
            mensajes= Mensajes(emisor_mensaje=request.user.username, receptor_mensaje='Todos', fecha_mensaje=date.today(), texto_mensaje=texto_msg, leido_mensaje=False, imagen_mensaje=imagen_msg)
            mensajes.save()
               
            usuarios=User.objects.values()
            try:
                imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url   
            except:
                return render(request, "AppNegocio/todosUsuarios.html",{"usuarios":usuarios})
            else:
                imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
                return render(request, "AppNegocio/todosUsuarios.html",{"usuarios":usuarios, "imagen":imagen})

                
    else:
        form=MensajeGlobalForm()  

    
    try:
         imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
    except:
        return render(request, "AppMensajes/mensajeGlobalFormulario.html",{"formulario":form})
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppMensajes/mensajeGlobalFormulario.html",{"formulario":form,"imagen":imagen})
    

@ login_required 
def chatGlobal(request):
    mensajes=Mensajes.objects.filter(receptor_mensaje='Todos')
    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url   
    except:
        return render(request, "AppMensajes/chatGlobal.html",{"mensajes":mensajes})
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppMensajes/chatGlobal.html",{"mensajes":mensajes, "imagen":imagen})
        
@ login_required
def marcarLeido(request, id):
    mensaje=Mensajes.objects.get(pk=id)
    mensaje.leido_mensaje=True
    mensaje.save
    mensajes=Mensajes.objects.filter(receptor_mensaje='Todos')
    

    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url   
    except:
        return render(request, "AppMensajes/chatGlobal.html",{"mensajes":mensajes})
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request,  "AppMensajes/chatGlobal.html",{"mensajes":mensajes, "imagen":imagen})


@ login_required
def mensajeIndivFormulario(request, tercero):
    if request.method =='POST':
        form=MensajeGlobalForm(request.POST, request.FILES)
        if form.is_valid():
            info=form.cleaned_data
            texto_msg=info["texto_msg"]
            imagen_msg=info["imagen_msg"]
            mensajes= Mensajes(emisor_mensaje=request.user.username, receptor_mensaje=tercero, fecha_mensaje=date.today(), texto_mensaje=texto_msg, leido_mensaje=False, imagen_mensaje=imagen_msg)
            mensajes.save()
            
               
            usuarios=User.objects.values()
            try:
                imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url   
            except:
                return render(request, "AppNegocio/todosUsuarios.html",{"usuarios":usuarios})
            else:
                imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
                return render(request, "AppNegocio/todosUsuarios.html",{"usuarios":usuarios, "imagen":imagen})

                
    else:
        form=MensajeGlobalForm()  

    
    try:
         imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
    except:
        return render(request, "AppMensajes/mensajeIndivFormulario.html",{"formulario":form})
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppMensajes/mensajeIndivFormulario.html",{"formulario":form,"imagen":imagen})
    
@ login_required 
def chatIndiv(request, username):
    mensajes=Mensajes.objects.filter(Q(emisor_mensaje=request.user.username, receptor_mensaje=username)|Q(emisor_mensaje=username, receptor_mensaje=request.user.username))
    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url   
    except:
        return render(request, "AppMensajes/chatIndiv.html",{"mensajes":mensajes})
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppMensajes/chatIndiv.html",{"mensajes":mensajes, "imagen":imagen})