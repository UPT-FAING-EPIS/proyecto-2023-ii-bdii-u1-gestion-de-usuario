from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('pizzas', views.pizzas, name='pizzas'),
    path('pizzas/crear', views.crear, name='crear'),
    path('pizzas/editar', views.editar, name='editar'),
]