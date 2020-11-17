from django.db import models

class cuenta(models.Model):
    tipo_cuenta = models.IntegerField( verbose_name='tipo cuenta')

class cliente(models.Model):
    usuario = models.CharField(max_length=15,verbose_name='usuario')
    contrasena = models.CharField(max_length=15,verbose_name='contraseña')
    nom_cliente = models.CharField(max_length=15,verbose_name='nombre cliente')
    correo = models.CharField(max_length=30, verbose_name='correo',null=True)
   
    

class cuadro(models.Model):
    id_cuadro = models.CharField( max_length=10, verbose_name='id cuadro')
    cuadro = models.CharField(max_length=20, verbose_name='cuadro')
    precio = models.CharField(max_length=15,verbose_name='precio')
