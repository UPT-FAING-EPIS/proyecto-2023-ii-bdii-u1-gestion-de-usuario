from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(Cargo)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(Empleado)
admin.site.register(Entrega)
admin.site.register(SesionUsuario)


