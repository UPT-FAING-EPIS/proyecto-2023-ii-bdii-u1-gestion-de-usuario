from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')




def pizzas(request):
    pizzas= Producto.objects.all()
    return(pizzas)
    #return render(request, 'pizzas/index.html', {'pizzas': pizzas})

def crear(request):
    return render(request, 'pizzas/crear.html')

def editar(request):
    return render(request, 'pizzas/editar.html')