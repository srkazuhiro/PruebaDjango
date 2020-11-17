from django.shortcuts import render
from django.http import HttpResponse
from frontend import models


# Create your views here.


def registrar(request):
    return render(request, 'registrar.html')

def mantenedorregistrar(request):

    usuario= 'sin usuario'
    if request.method=='POST':
        usuario=request.POST.get('usuario')
        contrasena=request.POST.get('contraseña')
        nom_cliente=request.POST.get('nombre cliente')
        correo=request.POST.get('correo')

        
        reg=models.cliente()
        reg.usuario=usuario
        reg.contrasena= contrasena
        reg.nom_cliente= nom_cliente
        reg.correo= correo
        reg.save()     
         
        return HttpResponse(usuario)


        