from django.urls import path
from .views import *



urlpatterns = [
    path('clientes/', clientes, name='clientes'),
    path('proveedores/', proveedores, name='proveedores'),
    path('articulos/', articulos, name='articulos'),
    path('',inicio,name='inicio'),
    path('clientesFormulario/', clientesFormulario, name='clientesFormulario'),
    path('proveedoresFormulario/', proveedoresFormulario, name='proveedoresFormulario'),
    path('articulosFormulario/', articulosFormulario, name='articulosFormulario'),
    path('busquedaClientes/', busquedaClientes, name='busquedaClientes'),
    path('buscarClientes/', buscarClientes,name="buscarClientes"),
    path('busquedaProveedores/', busquedaProveedores, name='busquedaProveedores'),
    path('buscarProveedores/', buscarProveedores, name='buscarProveedores'),
    path('busquedaArticulos/', busquedaArticulos, name='busquedaArticulos'),
    path('buscarArticulos/', buscarArticulos, name='buscarArticulos'),
]