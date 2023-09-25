from django.contrib import admin
from .models import Curso,Docente
# Register your models here.
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    #SIRVE PARA COLOCAR EL NOMBRE EN LA PARTE DE ARRIBA
    list_display=('id','nombre','creditos')

    #MOSTRAR DE FORMA DECRECIENTE
    #ordering=('-nombre',)

    #ES UN PANEL DE BUSQUEDA PARA BUSCAR POR NOMBRE O CREDITO
    search_fields=('nombre','creditos')

    #ESTO ES PARA EDITAR LOS CAMPOS EN LA MISMA PLANTILLA
    #list_editable=('nombre',)

    #ES UN HIPERVINCULO QUE VA DIRECTO AL EDITOR
    list_display_links=('nombre',)
    
admin.site.register(Docente)
#admin.site.register(Curso,CursoAdmin)

