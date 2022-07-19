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
            nombre=info["nombre"]
            tipo=info["tipo"]
            direccion=info["direccion"]
            email=info["email"]
            fecha_alta=info["fecha_alta"]
            clientes= Clientes(nombre_cli=nombre, tipo_cli=tipo, direccion_cli=direccion, email_cli=email, fecha_alta_cli=fecha_alta)
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
            nombre=info["nombre"]
            direccion=info["direccion"]
            email=info["email"]
            rubro=info["rubro"]
            fecha_alta=info["fecha_alta"]
            proveedores= Proveedores(nombre_prov=nombre, direccion_prov=direccion, email_prov=email, rubro_prov=rubro, fecha_alta_prov=fecha_alta)
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
            codigo_sku=info["codigo_sku"]
            nombre=info["nombre"]
            familia=info["familia"]
            stock=info["stock"]
            costo=info["costo"]
            precio_venta=info["precio_venta"]

            articulos= Articulos(codigo_sku_art=codigo_sku, nombre_art=nombre, familia_art=familia, stock_art=stock, costo_art=costo, precio_venta_art=precio_venta,)
            articulos.save()
            return render(request, "AppNegocio/inicio.html")
    else:
        form=ArticulosForm()  

    return render(request, "AppNegocio/articulosFormulario.html",{"formulario":form})

def busquedaClientes(request):
    return render(request, "AppNegocio/busquedaClientes.html")

def buscarClientes(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        clientes=Clientes.objects.filter(nombre_cli__icontains=nombre)
        return render(request,"AppNegocio/resultadosBusquedaClientes.html", {"clientes":clientes})
    else:
        respuesta = "No se ingresó ningún nombre de cliente"
    return render(request, "AppNegocio/resultadosBusquedaClientes.html",{"respuesta":respuesta})

def busquedaProveedores(request):
    return render(request, "AppNegocio/busquedaProveedores.html")

def buscarProveedores(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        proveedores=Proveedores.objects.filter(nombre_prov__icontains=nombre)
        return render(request,"AppNegocio/resultadosBusquedaProveedores.html", {"proveedores":proveedores})
    else:
        respuesta = "No se ingresó ningún nombre de proveedor"
    return render(request, "AppNegocio/resultadosBusquedaProveedores.html",{"respuesta":respuesta})

def busquedaArticulos(request):
    return render(request, "AppNegocio/busquedaArticulos.html")

def buscarArticulos(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        articulos=Articulos.objects.filter(nombre_art__icontains=nombre)
        return render(request,"AppNegocio/resultadosBusquedaArticulos.html", {"articulos":articulos})
    else:
        respuesta = "No se ingresó ningún nombre de artículo"
    return render(request, "AppNegocio/resultadosBusquedaProveedores.html",{"respuesta":respuesta})