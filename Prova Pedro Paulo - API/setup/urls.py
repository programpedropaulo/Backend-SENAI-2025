from django.urls import path
from aquarios_calcados.views import CompraAPIView,ProdutoAPIView


urlpatterns = [
    path('compra/', CompraAPIView.as_view()),
    path('produto/', ProdutoAPIView.as_view()),
]

