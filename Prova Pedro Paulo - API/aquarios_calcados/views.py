from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from aquarios_calcados.models import Compra,Produto
from aquarios_calcados.serializers import CompraSerializer,ProdutoSerializer

class ProdutoAPIView(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]

class CompraAPIView(generics.ListCreateAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)




