from rest_framework import serializers
from aquarios_calcados.models import Compra,Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

    def validate(self,validated_data):
       estoque = validated_data['quantidade_em_estoque']
       if estoque < 1:
           raise serializers.ValidationError("a quantidade de estoque deve ser maior que 0")

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'
        read_only_fields = ['usuario', 'data_de_inscricao']


    def validate(self,validated_data):
       estoque = validated_data['quantidade_em_estoque']
       quantidade = validated_data['quantidade']

       if quantidade <= 0:
           raise serializers.ValidationError("a quantidade deve ser maior que 0")
       if estoque < quantidade:
           raise serializers.ValidationError("o produto veio a acabar")

    def create(self, validated_data):
        produto = validated_data['produto']
        produto.quantidade_em_estoque -= 1
        produto.save()
        return super().create(validated_data)
