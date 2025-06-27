from rest_framework import serializers
from .models import Usuario

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["id","username", "senha"]


    
