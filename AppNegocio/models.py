from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre_cli = models.CharField(max_length=50)
    tipo_cli = models.CharField(max_length=50)
    direccion_cli = models.CharField(max_length=50)
    email_cli = models.EmailField()
    fecha_alta_cli= models.DateField()
    def __str__(self):
        return self.nombre_cli+" "+self.tipo_cli
    
class Proveedores(models.Model):
    nombre_prov = models.CharField(max_length=50)
    direccion_prov = models.CharField(max_length=50)
    email_prov = models.EmailField()
    rubro_prov = models.CharField(max_length=50)
    fecha_alta_prov= models.DateField()
    def __str__(self):
        return self.nombre_prov+" "+self.rubro_prov

class Articulos(models.Model):
    codigo_sku_art = models.CharField(max_length=50)
    nombre_art= models.CharField(max_length=50)
    familia_art= models.CharField(max_length=50)
    stock_art= models.IntegerField()
    costo_art= models.FloatField()
    precio_venta_art= models.FloatField()
    def __str__(self):
        return self.nombre_art+" SKU# ("+self.codigo_sku_art+")"




