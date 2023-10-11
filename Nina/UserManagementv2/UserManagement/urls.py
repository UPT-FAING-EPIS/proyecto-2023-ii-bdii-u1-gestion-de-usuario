from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers, permissions
from api import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Gestion Usuarios API",
        default_version='v1',
        description="Account Service",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@upt.pe"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('usuarios', views.UsuarioViewSet, 'usuarios')
router.register('permisos', views.PermisoViewSet, 'permisos')
router.register('roles', views.RolViewSet, 'roles')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('historial-rol/', views.HistorialRolListView.as_view(), name='historial-rol-list'),  # Vista basada en clase
    re_path(r'^historial-rol/(?P<pk>\d+)/$', views.HistorialRolDetailView.as_view(), name='historial-rol-detail'),  # Vista basada en clase
    path('usuarios-cambiar-rol/<int:pk>/', views.CambiarRolUsuarioView.as_view(), name='usuarios-cambiar-rol'),  # Vista basada en clase
]
