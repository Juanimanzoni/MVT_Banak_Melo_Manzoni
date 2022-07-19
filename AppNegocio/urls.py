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
    path('todosArticulos/', todosArticulos, name='todosArticulos'),
    path('todosClientes/', todosClientes, name='todosClientes'),
    path('todosProveedores/', todosProveedores, name='todosProveedores'),
    path('eliminarClientes/<nombre_clientes>',eliminarClientes,name='eliminarClientes'),
    path('eliminarArticulos/<nombre_articulos>',eliminarArticulos,name='eliminarArticulos'),
    path('eliminarProveedores/<nombre_proveedores>',eliminarProveedores,name='eliminarProveedores'),
    path('editarClientes/<nombre_clientes>', editarClientes, name='editarClientes'),
    path('editarArticulos/<nombre_articulos>', editarArticulos, name='editarArticulos'),
    path('editarProveedores/<nombre_proveedores>', editarProveedores, name='editarProveedores'),
]