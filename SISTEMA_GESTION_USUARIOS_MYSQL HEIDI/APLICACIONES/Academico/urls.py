from django.urls import path
from APLICACIONES.Academico.views import CursoListView

urlpatterns=[
    path('', CursoListView.as_view(),name='gestion_cursos')
]