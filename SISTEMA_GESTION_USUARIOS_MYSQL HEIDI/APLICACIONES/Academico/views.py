from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from .models import Curso
# Create your views here.

def home(request):
    cursosListados=Curso.objects.all().order_by('nombre') #API
    # cursosListados = Curso.objects.all()
    # cursosListados = Curso.objects.all()[:5] 
    # cursosListados = Curso.objects.all()[4:9]
    # cursosListados = Curso.objects.all().order_by('nombre')
    # cursosListados = Curso.objects.all().order_by('-nombre')
    # cursosListados = Curso.objects.all().order_by('nombre', 'creditos')
    # cursosListados = Curso.objects.filter(nombre= 'Historia', creditos=5)
    # cursosListados = Curso.objects.filter(creditos_lte=4)
    # cursostistados = Curso.objects.filter(nombre_startswith= 'Q')
    # cursosListados = Curso.objects.filter(nombre_contains='g')

    data={
        'titulo':'GESTION DE USUARIOS',
        'cursos': cursosListados
    }
    return render(request,"gestionCurso.html", data)

#ES UNA MEJOR FORMA DE TRABAJAR CON VISTAS EN PYTHON
class CursoListView(ListView):
    model= Curso
    template_name='gestionCurso.html'

    def get_context_data(self, **kwargs):
        
        context= super().get_context_data(**kwargs)
        context['titulo']='GESTION DE USUARIOS'
        #print(context)
        return context