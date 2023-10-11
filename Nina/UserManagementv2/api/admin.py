from django.contrib import admin
from .models import Usuario, Rol, Permiso, HistorialRol

class HistorialRolInline(admin.TabularInline):
    model = HistorialRol
    extra = 0
    readonly_fields = ('usuario', 'rol_anterior', 'rol_nuevo', 'fecha_cambio')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'full_name', 'created_at', 'role')
    search_fields = ('username', 'email', 'full_name')
    list_filter = ('role',)
    inlines = [HistorialRolInline]

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('role_id', 'role_name')
    search_fields = ('role_name',)

@admin.register(Permiso)
class PermisoAdmin(admin.ModelAdmin):
    list_display = ('permiso_id', 'role', 'permiso_name')
    search_fields = ('permiso_name', 'role__role_name')
    list_filter = ('role',)
