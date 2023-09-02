from django.db import models

# Tabla de Cargos
class Cargo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_cargo = models.CharField(max_length=100, verbose_name='Nombre del Cargo')

    def __str__(self):
        return self.nombre_cargo

# Tabla de Clientes
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()

    def __str__(self):
        dcli="Cliente : " + self.nombre + " " + self.apellido + " Dir: " + self.direccion + "Telf: " +self.telefono
        # return f'{self.nombre} {self.apellido}'      es la personalizacion de como llamar los datos al admin del sistema que lo ve todo
        return dcli

# Tabla de Productos
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen", null=True, blank=True)

    def __str__(self):
        return self.nombre
    #instruccion para borrar la imagen del storage y a la vez borrarlo en la web
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()



# Tabla de Pedidos
class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_hora_pedido = models.DateTimeField(auto_now_add=True)
    estado_pedido = models.CharField(max_length=100)

    def __str__(self):
        return f'Pedido #{self.id} - Cliente: {self.cliente}'

# Tabla de Detalles de Pedido
class DetallePedido(models.Model):
    id = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

# Tabla de Empleados
class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=15)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

# Tabla de Entregas (opcional, si entregan a domicilio)
class Entrega(models.Model):
    id = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    direccion_entrega = models.TextField()
    fecha_hora_entrega = models.DateTimeField()

# Tabla de Sesiones de Usuarios
class SesionUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    token_sesion = models.CharField(max_length=100)
    fecha_hora_inicio_sesion = models.DateTimeField()
    fecha_hora_fin_sesion = models.DateTimeField(null=True)

    def __str__(self):
        return f'Sesión de {self.empleado}'

