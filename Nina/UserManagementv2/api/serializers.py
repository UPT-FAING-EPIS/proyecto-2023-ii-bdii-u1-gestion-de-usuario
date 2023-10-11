from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import Usuario, Permiso, Rol, HistorialRol

class LetrasValidator:
    def __call__(self, value):
        if not value.replace(" ", "").isalpha():
            raise serializers.ValidationError('Solo se permiten letras y espacios.')

class UsuarioSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=100, validators=[LetrasValidator()])
    email = serializers.CharField(max_length=255)  # Cambiado de EmailField a CharField
    role_name = serializers.CharField(source='role.role_name', read_only=True)
    historial_roles = serializers.SerializerMethodField()

    class Meta:
        model = Usuario
        fields = '__all__'

    def get_historial_roles(self, instance):
        historial_roles = HistorialRol.objects.filter(usuario=instance)
        return HistorialRolSerializer(historial_roles, many=True).data

class PermisoSerializer(serializers.ModelSerializer):
    permiso_name = serializers.CharField(max_length=50, validators=[LetrasValidator()])

    class Meta:
        model = Permiso
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(max_length=50, validators=[LetrasValidator()])

    class Meta:
        model = Rol
        fields = '__all__'

class HistorialRolSerializer(serializers.ModelSerializer):
    usuario_username = serializers.CharField(source='usuario.username', read_only=True)
    rol_anterior_name = serializers.CharField(source='rol_anterior', read_only=True)
    rol_nuevo_name = serializers.CharField(source='rol_nuevo', read_only=True)

    class Meta:
        model = HistorialRol
        fields = '__all__'
