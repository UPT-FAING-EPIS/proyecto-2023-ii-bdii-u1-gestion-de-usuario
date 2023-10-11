from django.db import models
from django.core.validators import RegexValidator

class Rol(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=50, unique=True, validators=[RegexValidator(r'^[a-zA-Z]*$', 'Solo se permiten letras.')])

    def __str__(self):
        return self.role_name

class Permiso(models.Model):
    permiso_id = models.AutoField(primary_key=True)
    role = models.ForeignKey(Rol, on_delete=models.CASCADE)
    permiso_name = models.CharField(max_length=50, validators=[RegexValidator(r'^[a-zA-Z]*$', 'Solo se permiten letras.')])

    def __str__(self):
        return self.permiso_name

class Usuario(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)  # Cambiado de EmailField a CharField
    full_name = models.CharField(max_length=100, validators=[RegexValidator(r'^[a-zA-Z ]*$', 'Solo se permiten letras y espacios.')])
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

    def cambiar_rol(self, nuevo_rol):
        rol_anterior = self.role.role_name
        historial = HistorialRol(usuario=self, rol_anterior=rol_anterior, rol_nuevo=nuevo_rol)
        historial.save()
        self.role = nuevo_rol
        self.save()

class HistorialRol(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    rol_anterior = models.CharField(max_length=50)
    rol_nuevo = models.CharField(max_length=50)
    fecha_cambio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username}: {self.rol_anterior} -> {self.rol_nuevo}"
