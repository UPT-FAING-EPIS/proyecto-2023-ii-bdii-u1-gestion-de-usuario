from rest_framework import viewsets, mixins, generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, Permiso, Rol, HistorialRol
from .serializers import UsuarioSerializer, PermisoSerializer, RolSerializer, HistorialRolSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PermisoViewSet(viewsets.ModelViewSet):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class HistorialRolListView(generics.ListAPIView):
    queryset = HistorialRol.objects.all()
    serializer_class = HistorialRolSerializer

class HistorialRolDetailView(generics.RetrieveAPIView):
    queryset = HistorialRol.objects.all()
    serializer_class = HistorialRolSerializer

class CambiarRolUsuarioView(generics.UpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        nuevo_rol_id = request.data.get('role', None)  # Cambiado de 'nuevo_rol_id' a 'role'

        if nuevo_rol_id is None:
            return Response({'error': 'Debe proporcionar un nuevo ID de rol'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            nuevo_rol = Rol.objects.get(role_id=nuevo_rol_id)
        except Rol.DoesNotExist:
            return Response({'error': 'Rol no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        instance.cambiar_rol(nuevo_rol)

        serializer = self.get_serializer(instance, partial=partial)
        return Response(serializer.data)
