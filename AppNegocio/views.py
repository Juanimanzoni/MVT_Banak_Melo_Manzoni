from ast import Return
from this import d
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
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model #ver si es necesario

# Create your views here.
def inicio(request):
    #return render(request, "AppNegocio/inicio.html")
    
    if (str(Avatar.objects.filter(user= request.user.id))!="<QuerySet []>"):
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/inicio.html", {"imagen":imagen})
    else:
        return render(request, "AppNegocio/inicio.html")

       
    


def clientes(request):
    if not request.user.is_authenticated:
        return render(request, "AppNegocio/inicio.html",{"mensaje":"Debe ingresar con su usuario y clave para poder acceder a Clientes - En caso de no tener usuario, regístrese."})
    else:
        try:
            imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        except:
            return render(request, "AppNegocio/clientes.html")
        else:
            imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
            return render(request, "AppNegocio/clientes.html", {"imagen":imagen})





def proveedores(request):
    if not request.user.is_authenticated:
        return render(request, "AppNegocio/inicio.html",{"mensaje":"Debe ingresar con su usuario y clave para poder acceder a Proveedores - En caso de no tener usuario, regístrese."})
    else:
        try:
            imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        except:
            return render(request, "AppNegocio/proveedores.html")
        else:
            imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
            return render(request, "AppNegocio/proveedores.html", {"imagen":imagen})




def articulos(request):
    if not request.user.is_authenticated:
        return render(request, "AppNegocio/inicio.html",{"mensaje":"Debe ingresar con su usuario y clave para poder acceder a Artículos - En caso de no tener usuario, regístrese."})
    else:
        try:
            imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        except:
            return render(request, "AppNegocio/articulos.html")
        else:
            imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
            return render(request, "AppNegocio/articulos.html", {"imagen":imagen})


@ login_required
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
            
            try:
                imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
            except:
                return render(request, "AppNegocio/inicio.html")
            else:
                imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
                return render(request, "AppNegocio/inicio.html", {"imagen":imagen})
    
    else:
        form=ClientesForm()  

    
    try:
         imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
    except:
        return render(request, "AppNegocio/clientesFormulario.html",{"formulario":form})
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/clientesFormulario.html",{"formulario":form,"imagen":imagen})
    

@ login_required
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
            try:
                imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
            except:
                return render(request, "AppNegocio/inicio.html")
            else:
                imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
                return render(request, "AppNegocio/inicio.html", {"imagen":imagen})
   
    else:
        form=ProveedoresForm()  
    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
    except:
        return render(request, "AppNegocio/proveedoresFormulario.html",{"formulario":form})
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/proveedoresFormulario.html", {"formulario":form, "imagen":imagen})
        
@ login_required
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
            
            try:
                imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
            except:
                return render(request, "AppNegocio/inicio.html")
            else:
                imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
                return render(request, "AppNegocio/inicio.html", {"imagen":imagen})
   
    else:
        form=ArticulosForm()  
    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
    except:
        return render(request, "AppNegocio/articulosFormulario.html",{"formulario":form})
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/articulosFormulario.html", {"formulario":form, "imagen":imagen})
        
        
@ login_required
def busquedaClientes(request):
    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
    except:
        return render(request, "AppNegocio/busquedaClientes.html")
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/busquedaClientes.html", {"imagen":imagen})



@ login_required
def buscarClientes(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        clientes=Clientes.objects.filter(nombre_cli__icontains=nombre)
        
        try:
            imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        except:
            return render(request,"AppNegocio/resultadosBusquedaClientes.html", {"clientes":clientes})
        else:
            imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
            return render(request, "AppNegocio/resultadosBusquedaClientes.html", {"clientes":clientes, "imagen":imagen})
                     
    else:
        respuesta = "No se ingresó ningún nombre de cliente"
    
    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url   
    except:
        return render(request, "AppNegocio/resultadosBusquedaClientes.html",{"respuesta":respuesta})
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/resultadosBusquedaClientes.html",{"respuesta":respuesta, "imagen":imagen})

  
@ login_required
def busquedaProveedores(request):
    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
    except:
        return render(request, "AppNegocio/busquedaProveedores.html")
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/busquedaProveedores.html", {"imagen":imagen})
    
        
    
@ login_required
def buscarProveedores(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        proveedores=Proveedores.objects.filter(nombre_prov__icontains=nombre)
        
        try:
            imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        except:
            return render(request,"AppNegocio/resultadosBusquedaProveedores.html", {"proveedores":proveedores})
        else:
            imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
            return render(request, "AppNegocio/resultadosBusquedaProveedores.html", {"proveedores":proveedores, "imagen":imagen})
       
    else:
        respuesta = "No se ingresó ningún nombre de proveedor"
    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url   
    except:
        return render(request, "AppNegocio/resultadosBusquedaProveedores.html",{"respuesta":respuesta})
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/resultadosBusquedaProveedores.html",{"respuesta":respuesta, "imagen":imagen})

    
@ login_required
def busquedaArticulos(request):
    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
    except:
        return render(request, "AppNegocio/busquedaArticulos.html")
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/busquedaArticulos.html", {"imagen":imagen})
    
        
   
@ login_required
def buscarArticulos(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        articulos=Articulos.objects.filter(nombre_art__icontains=nombre)
        
        try:
            imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        except:
            return render(request,"AppNegocio/resultadosBusquedaArticulos.html", {"articulos":articulos})
        else:
            imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
            return render(request, "AppNegocio/resultadosBusquedaArticulos.html", {"articulos":articulos, "imagen":imagen})

              
    else:
        respuesta = "No se ingresó ningún nombre de artículo"
    
    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url   
    except:
        return render(request, "AppNegocio/resultadosBusquedaArticulos.html",{"respuesta":respuesta})
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/resultadosBusquedaArticulos.html",{"respuesta":respuesta, "imagen":imagen})

    
    
@ login_required 
def todosClientes(request):
    clientes=Clientes.objects.all()
    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url   
    except:
        return render(request, "AppNegocio/todosClientes.html",{"clientes":clientes})
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/todosClientes.html",{"clientes":clientes, "imagen":imagen})


    
@ login_required
def todosProveedores(request):
    proveedores=Proveedores.objects.all()
    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url   
    except:
        return render(request, "AppNegocio/todosProveedores.html",{"proveedores":proveedores})
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/todosProveedores.html",{"proveedores":proveedores, "imagen":imagen})
    
    
@ login_required    
def todosArticulos(request):
    articulos=Articulos.objects.all()
    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url   
    except:
        return render(request, "AppNegocio/todosArticulos.html",{"articulos":articulos})
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/todosArticulos.html",{"articulos":articulos, "imagen":imagen})
    
    
    
@ login_required
def eliminarClientes(request, nombre_clientes):
    cliente=Clientes.objects.get(nombre_cli=nombre_clientes)
    cliente.delete()
    clientes=Clientes.objects.all()
    
    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url   
    except:
        return render(request, "AppNegocio/todosClientes.html",{"clientes":clientes})
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/todosClientes.html",{"clientes":clientes, "imagen":imagen})
    
    
    
@ login_required  
def eliminarProveedores(request, nombre_proveedores):
    proveedor=Proveedores.objects.get(nombre_prov=nombre_proveedores)
    proveedor.delete()
    proveedores=Proveedores.objects.all()
    
    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url   
    except:
        return render(request, "AppNegocio/todosProveedores.html",{"proveedores":proveedores})
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/todosProveedores.html",{"proveedores":proveedores, "imagen":imagen})
    
    
    
@ login_required
def eliminarArticulos(request, nombre_articulos):
    articulo= Articulos.objects.get(nombre_art=nombre_articulos)
    articulo.delete()
    articulos= Articulos.objects.all()
    
    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url   
    except:
        return render(request, "AppNegocio/todosArticulos.html",{"articulos":articulos})
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/todosArticulos.html",{"articulos":articulos, "imagen":imagen})
    
    
    
@ login_required
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
            
            try:
                imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
            except:
                return render(request, "AppNegocio/clientes.html")
            else:
                imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
                return render(request, "AppNegocio/clientes.html",{"imagen":imagen})
            
    else:
        form=ClientesForm(initial={"nombre":cliente.nombre_cli, "tipo":cliente.tipo_cli, "direccion":cliente.direccion_cli, "email":cliente.email_cli, "fecha_alta":cliente.fecha_alta_cli})
  
    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url   
    except:
        return render(request, "AppNegocio/editarClientes.html",{"formulario":form, "nombre_clientes":nombre_clientes})
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/editarClientes.html",{"formulario":form, "nombre_clientes":nombre_clientes, "imagen":imagen})
    
    
    
@ login_required    
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
            
            try:
                imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
            except:
                return render(request, "AppNegocio/inicio.html")
            else:
                imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
                return render(request, "AppNegocio/inicio.html",{"imagen":imagen})

            
              
    else:
        form=ArticulosForm(initial={"codigo_sku":articulo.codigo_sku_art, "nombre":articulo.nombre_art, "familia":articulo.familia_art, "stock":articulo.stock_art, "costo":articulo.costo_art,"precio_venta":articulo.precio_venta_art })
    
    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url   
    except:
        return render(request, "AppNegocio/editarArticulos.html",{"formulario":form, "nombre_articulos":nombre_articulos})
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/editarArticulos.html",{"formulario":form, "nombre_articulos":nombre_articulos, "imagen":imagen})

  
@ login_required
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
            try:
                imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
            except:
                return render(request, "AppNegocio/inicio.html")
            else:
                imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
                return render(request, "AppNegocio/inicio.html",{"imagen":imagen})

                    
    else:
        form=ProveedoresForm(initial={"nombre":proveedor.nombre_prov, "direccion":proveedor.direccion_prov, "email":proveedor.email_prov, "rubro":proveedor.rubro_prov, "fecha_alta":proveedor.fecha_alta_prov})
    
    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url   
    except:
        return render(request, "AppNegocio/editarProveedores.html",{"formulario":form, "nombre_proveedores":nombre_proveedores})
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/editarProveedores.html",{"formulario":form, "nombre_proveedores":nombre_proveedores, "imagen":imagen})

    
   

def login_request(request):

    if request.method=="POST":
        form=AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usu= request.POST['username']
            clave = request.POST['password']
            usuario = authenticate(username=usu, password=clave)

            if usuario is not None:
                login(request, usuario)
                
                try:
                    imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
                except:
                    return render(request, "AppNegocio/inicio.html",{'form':form, 'mensaje':f'Bienvenido {usuario}'})
                else:
                    imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
                    return render(request, "AppNegocio/inicio.html", {'form':form, 'mensaje':f'Bienvenido {usuario}', "imagen":imagen})

                
            else:
                try:
                    imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
                except:
                    return render(request, 'AppNegocio/login.html',{'form':form, 'mensaje':'Usuario o clave incorrectos'})
                else:
                    imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
                    return render(request, 'AppNegocio/login.html',{'form':form, 'mensaje':'Usuario o clave incorrectos', "imagen":imagen})

               
                
        else:
            try:
                imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url          
            except:
                return render(request, 'AppNegocio/login.html',{'form':form, 'mensaje':'Formulario invalido'})
            else:
                imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
                return render(request, 'AppNegocio/login.html',{'form':form, 'mensaje':'Formulario invalido', "imagen":imagen})
            
        
    else:
        form=AuthenticationForm()
        
        try:
            imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url          
        except:
            return render(request, 'AppNegocio/login.html',{'form':form})
        else:
            imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
            return render(request, 'AppNegocio/login.html',{'form':form, "imagen":imagen})
            
  

def register(request):

    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            form.save()
                
            
            try:
                imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
            except:
                return render(request, 'AppNegocio/inicio.html',{'form':form, 'mensaje':f'Usuario Creado: {username}'})
            else:
                imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
                return render(request, 'AppNegocio/inicio.html',{'form':form, 'mensaje':f'Usuario Creado: {username}', "imagen":imagen})
            
           
    else:
        form=UserRegisterForm()
    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
    except:
        return render(request, "AppNegocio/register.html",{'form':form})
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/register.html", {'form':form,  "imagen":imagen})


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
            try:
                imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
            except:
                return render(request, "AppNegocio/inicio.html",{'usuario':usuario, 'mensaje':'Perfil Editado Exitosamente'})
            else:
                imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
                return render(request, "AppNegocio/inicio.html", {'usuario':usuario, 'mensaje':'Perfil Editado Exitosamente', "imagen":imagen})

    else:
        formulario=UserEditForm(instance=usuario)
    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
    except:
        return render(request, "AppNegocio/editarPerfil.html",{'formulario':formulario, 'usuario':usuario.username})
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/editarPerfil.html", {'formulario':formulario, 'usuario':usuario.username, "imagen":imagen})

    
   



@ login_required
def agregarAvatar(request):
    if request.method == 'POST':
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            
            try:#si el user no tenia avatar pitaba porque no podia asignar avatar viejo
                Avatar.objects.get(user=request.user)
            except:
                avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
                avatar.save()

                if (str(Avatar.objects.filter(user= request.user.id))!="<QuerySet []>"):
                    imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
                    return render(request, 'AppNegocio/inicio.html', {'usuario':request.user, 'mensaje':'Avatar agregado exitosamente', "imagen":imagen})
                else:
                    return render(request, 'AppNegocio/inicio.html', {'usuario':request.user, 'mensaje':'Avatar agregado exitosamente'})
                
                
                
            else:#si no pito borro anterior
                avatarViejo=Avatar.objects.get(user=request.user)
                if(avatarViejo.imagen):
                    avatarViejo.delete()
                avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
                avatar.save()

                if (str(Avatar.objects.filter(user= request.user.id))!="<QuerySet []>"):
                    imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
                    return render(request, 'AppNegocio/inicio.html', {'usuario':request.user, 'mensaje':'Avatar agregado exitosamente', "imagen":imagen})
                else:
                    return render(request, 'AppNegocio/inicio.html', {'usuario':request.user, 'mensaje':'Avatar agregado exitosamente'})
          
    else:
        formulario=AvatarForm()
    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
    except:
        return render(request, "AppNegocio/agregarAvatar.html",{'formulario':formulario, 'usuario':request.user})
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/agregarAvatar.html", {'formulario':formulario, 'usuario':request.user, "imagen":imagen})
    
   
def about(request):
    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
    except:
        return render(request, "AppNegocio/about.html")
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/about.html", {"imagen":imagen})#ver si paso las otras imagenes

@ login_required 
def todosUsuarios(request):

    #print(request.user.username)
            

    usuarios=User.objects.values()
    try:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url   
    except:
        return render(request, "AppNegocio/todosUsuarios.html",{"usuarios":usuarios})
    else:
        imagen=Avatar.objects.filter(user= request.user.id)[0].imagen.url
        return render(request, "AppNegocio/todosUsuarios.html",{"usuarios":usuarios, "imagen":imagen})


