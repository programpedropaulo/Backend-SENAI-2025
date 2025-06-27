
from rest_framework import generics
from .models import Usuario
from .serializers import  UserModelSerializer

class UsuarioAPIViews(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserModelSerializer