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
    
]