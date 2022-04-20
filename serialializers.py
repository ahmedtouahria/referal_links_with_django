from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class CreateUserSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name', 'username')
        password = serializers.CharField(
            style={'input_type': 'password'}, min_length=8, max_length=100, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

