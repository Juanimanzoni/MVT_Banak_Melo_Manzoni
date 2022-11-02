from django.urls import path, include
from .views import *
from AppNegocio.views import *
from django.contrib.auth.views import LogoutView




urlpatterns = [
        path('mensajeGlobalFormulario/', mensajeGlobalFormulario, name='mensajeGlobalFormulario'),
        path('chatGlobal/', chatGlobal, name='chatGlobal'),
        path('marcarLeido/<id>',marcarLeido,name='marcarLeido'),
        path('mensajeIndivFormulario/', mensajeIndivFormulario, name='mensajeIndivFormulario'),
        path('chatIndiv/', chatIndiv, name='chatIndiv'),
]
