
#===============================================================
#                         Exercicio 3
#===============================================================
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserModelSerializer 
from django.contrib.auth.hashers import make_password
from .models import Usuario
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

#===============================================================
#                         Exercicio 3
#===============================================================
@api_view(["GET", "POST", "PUT", "DELETE"])
def criar_usuario(request):
    if request.method == "GET":
        usuarios = Usuario.objects.all()
        serializer = UserModelSerializer(usuarios, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = UserModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['senha'] = make_password(serializer.validated_data['senha'])
            user = serializer.save()
            return Response({
                "id": user.id,
                "username": user.username
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        return Response({"mensagem": "Método PUT ainda não implementado"}, status=200)

    elif request.method == "DELETE":
        return Response({"mensagem": "Método DELETE ainda não implementado"}, status=200)
    
#===============================================================
#                         Exercicio 4
#===============================================================

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def rota_protegida(request):
    return Response({"mensagem": "Acesso autorizado com Basic Auth"})

