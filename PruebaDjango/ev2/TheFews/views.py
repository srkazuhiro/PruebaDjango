
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request,'index.html')

def nintendo(request):
    return render(request,'pagina2.html')


def login(request):
    return render(request,'login.html')

def registrar(request):
    return render(request,'registrar.html')