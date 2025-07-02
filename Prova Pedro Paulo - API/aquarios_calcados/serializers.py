from rest_framework import serializers
from aquarios_calcados.models import Compra,Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'
        read_only_fields = ['usuario', 'data_de_inscricao']


    def validate(self, data):
        produto = data['produto']
        if produto.quantidade_em_estoque <= 0:
            raise serializers.ValidationError("Este produto nâo está mais disponivel.")
        return data

    def create(self, validated_data):
        produto = validated_data['produto']
        produto.quantidade_em_estoque -= 1
        produto.save()
        return super().create(validated_data)
