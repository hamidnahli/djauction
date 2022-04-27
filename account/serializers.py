from django.contrib.auth.password_validation import validate_password

from authentication.models import User
from rest_framework import serializers


class RetrieveUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'bidder_id', 'username', 'email', 'title', 'first_name', 'last_name', 'address', 'city', 'zipcode',
            'country', 'phone',
            'office_phone', 'company',)
        read_only_fields = ('id', 'last_login', 'is_superuser', 'created_at', 'updated_at', 'username', 'email')


class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'title', 'first_name', 'last_name', 'address', 'city', 'zipcode',
            'country', 'phone',
            'office_phone', 'company',)


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance
