from ast import Return
from django import http
from django.shortcuts import render
from AppNegocio.models import Clientes, Proveedores, Articulos
from django.http import HttpResponse
from AppNegocio.forms import *
import datetime


# Create your views here.
def inicio(request):
    return render(request, "AppNegocio/inicio.html")

def clientes(request):
     return render(request, "AppNegocio/clientes.html")

def proveedores(request):
     return render(request, "AppNegocio/proveedores.html")

def articulos(request):
     return render(request, "AppNegocio/articulos.html")

def clientesFormulario(request):
    if request.method =='POST':
        form=ClientesForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre_cli=info["nombre_cli"]
            tipo_cli=info["tipo_cli"]
            direccion_cli=info["direccion_cli"]
            email_cli=info["email_cli"]
            fecha_alta_cli=info["fecha_alta_cli"]
            clientes= Clientes(nombre_cli=nombre_cli, tipo_cli=tipo_cli, direccion_cli=direccion_cli, email_cli=email_cli, fecha_alta_cli=fecha_alta_cli)
            clientes.save()
            return render(request, "AppNegocio/inicio.html")
    else:
        form=ClientesForm()  

    return render(request, "AppNegocio/clientesFormulario.html",{"formulario":form})

def proveedoresFormulario(request):
    if request.method =='POST':
        form=ProveedoresForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre_prov=info["nombre_prov"]
            direccion_prov=info["direccion_prov"]
            email_prov=info["email_prov"]
            rubro_prov=info["rubro_prov"]
            fecha_alta_prov=info["fecha_alta_prov"]
            proveedores= Proveedores(nombre_prov=nombre_prov, direccion_prov=direccion_prov, email_prov=email_prov, rubro_prov=rubro_prov, fecha_alta_prov=fecha_alta_prov)
            proveedores.save()
            return render(request, "AppNegocio/inicio.html")
    else:
        form=ProveedoresForm()  

    return render(request, "AppNegocio/proveedoresFormulario.html",{"formulario":form})

def articulosFormulario(request):
    if request.method =='POST':
        form=ArticulosForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            codigo_sku_art=info["codigo_sku_art"]
            nombre_art=info["nombre_art"]
            familia_art=info["familia_art"]
            stock_art=info["stock_art"]
            costo_art=info["costo_art"]
            precio_venta_art=info["precio_venta_art"]

            articulos= Articulos(codigo_sku_art=codigo_sku_art, nombre_art=nombre_art, familia_art=familia_art, stock_art=stock_art, costo_art=costo_art, precio_venta_art=precio_venta_art,)
            articulos.save()
            return render(request, "AppNegocio/inicio.html")
    else:
        form=ArticulosForm()  

    return render(request, "AppNegocio/articulosFormulario.html",{"formulario":form})


