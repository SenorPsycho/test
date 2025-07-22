from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name', 'email', 'contact','password']

        extra_kwargs = {
            'password': {'write_only' : True},
            'email' : {'required' : True},
        }