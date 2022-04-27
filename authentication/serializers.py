from abc import ABC

from authentication.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=50, write_only=True)

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'address',
            'zipcode',
            'city',
            'phone',
            'country',
        )


class LogInSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        user_data = RegisterSerializer(user).data
        for key, value in user_data.items():
            if key != 'id':
                token[key] = value
        return token
