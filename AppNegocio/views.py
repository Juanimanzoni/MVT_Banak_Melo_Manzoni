from ast import Return
from django import http
from django.shortcuts import render
from AppNegocio.models import *
from django.http import HttpResponse
from AppNegocio.forms import *
import datetime
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
def inicio(request):
    
    if Avatar.objects.filter(user= request.user.id) is not None:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/inicio.html", {"imagen":imagen}) #, {"imagen":imagen}
    else:
        return render(request, "AppNegocio/inicio.html")
def clientes(request):
     return render(request, "AppNegocio/clientes.html")

@login_required
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

def todosClientes(request):
    clientes=Clientes.objects.all()
    return render (request, "AppNegocio/todosClientes.html",{"clientes":clientes})

def todosProveedores(request):
    proveedores=Proveedores.objects.all()
    return render (request, "AppNegocio/todosProveedores.html",{"proveedores":proveedores})

def todosArticulos(request):
    articulos=Articulos.objects.all()
    return render (request, "AppNegocio/todosArticulos.html",{"articulos":articulos})

def eliminarClientes(request, nombre_clientes):
    cliente=Clientes.objects.get(nombre_cli=nombre_clientes)
    cliente.delete()
    clientes=Clientes.objects.all()
    return render (request, "AppNegocio/todosClientes.html",{"clientes":clientes})

def eliminarProveedores(request, nombre_proveedores):
    proveedor=Proveedores.objects.get(nombre_prov=nombre_proveedores)
    proveedor.delete()
    proveedores=Proveedores.objects.all()
    return render (request, "AppNegocio/todosProveedores.html",{"proveedores":proveedores})

def eliminarArticulos(request, nombre_articulos):
    articulo= Articulos.objects.get(nombre_art=nombre_articulos)
    articulo.delete()
    articulos= Articulos.objects.all()
    return render (request, "AppNegocio/todosArticulos.html",{"articulos":articulos})

def editarClientes(request, nombre_clientes):
    cliente=Clientes.objects.get(nombre_cli=nombre_clientes)
    if request.method=="POST":
        form=ClientesForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            cliente.nombre_cli=info["nombre"]
            cliente.tipo_cli=info["tipo"]
            cliente.direccion_cli=info["direccion"]
            cliente.email_cli=info["email"]
            cliente.fecha_alta_cli=info["fecha_alta"]
            cliente.save()
            return render(request, "AppNegocio/inicio.html")
    else:
        form=ClientesForm(initial={"nombre":cliente.nombre_cli, "tipo":cliente.tipo_cli, "direccion":cliente.direccion_cli, "email":cliente.email_cli, "fecha_alta":cliente.fecha_alta_cli})
    return render(request, "AppNegocio/editarClientes.html",{"formulario":form, "nombre_clientes":nombre_clientes})


def editarArticulos(request, nombre_articulos):
    articulo=Articulos.objects.get(nombre_art=nombre_articulos)
    if request.method=="POST":
        form=ArticulosForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            articulo.codigo_sku_art=info["codigo_sku"]
            articulo.nombre_art=info["nombre"]
            articulo.familia_art=info["familia"]
            articulo.stock_art=info["stock"]
            articulo.costo_art=info["costo"]
            articulo.precio_venta_art=info["precio_venta"]
            articulo.save()
            return render(request, "AppNegocio/inicio.html")
    else:
        form=ArticulosForm(initial={"codigo_sku":articulo.codigo_sku_art, "nombre":articulo.nombre_art, "familia":articulo.familia_art, "stock":articulo.stock_art, "costo":articulo.costo_art,"precio_venta":articulo.precio_venta_art })
    return render(request, "AppNegocio/editarArticulos.html",{"formulario":form, "nombre_articulos":nombre_articulos})



def editarProveedores(request, nombre_proveedores):
    proveedor=Proveedores.objects.get(nombre_prov=nombre_proveedores)
    if request.method=="POST":
        form=ProveedoresForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            proveedor.nombre_prov=info["nombre"]
            proveedor.direccion_prov=info["direccion"]
            proveedor.email_prov=info["email"]
            proveedor.rubro_prov=info["rubro"]
            proveedor.fecha_alta_prov=info["fecha_alta"]
            proveedor.save()
            return render(request, "AppNegocio/inicio.html")
    else:
        form=ProveedoresForm(initial={"nombre":proveedor.nombre_prov, "direccion":proveedor.direccion_prov, "email":proveedor.email_prov, "rubro":proveedor.rubro_prov, "fecha_alta":proveedor.fecha_alta_prov})
    return render(request, "AppNegocio/editarProveedores.html",{"formulario":form, "nombre_proveedores":nombre_proveedores})


def login_request(request):

    if request.method=="POST":
        form=AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usu= request.POST['username']
            clave = request.POST['password']
            usuario = authenticate(username=usu, password=clave)

            if usuario is not None:
                login(request, usuario)
                return render(request, 'AppNegocio/inicio.html',{'form':form, 'mensaje':f'Bienvenido {usuario}'})

            else:
                return render(request, 'AppNegocio/login.html',{'form':form, 'mensaje':'Usuario o clave incorrectos'})
        else:
            return render(request, 'AppNegocio/login.html',{'form':form, 'mensaje':'Formulario invalido'})
    else:
        form=AuthenticationForm()
        return render(request, 'AppNegocio/login.html',{'form':form})


def register(request):

    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            form.save()
            return render(request, 'AppNegocio/inicio.html',{'form':form, 'mensaje':f'Usuario Creado: {username}'})

           
    else:
        form=UserRegisterForm()
    return render(request, 'AppNegocio/register.html',{'form':form})

@login_required
def editarPerfil(request):
    usuario=request.user

    if request.method == 'POST':
        formulario=UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()

            return render(request, 'AppNegocio/inicio.html', {'usuario':usuario, 'mensaje':'PERFIL EDITADO EXITOSAMENTE'})
    else:
        formulario=UserEditForm(instance=usuario)
    return render(request, 'AppNegocio/editarPerfil.html', {'formulario':formulario, 'usuario':usuario.username})
