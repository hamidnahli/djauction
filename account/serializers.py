from authentication.models import User
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _


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


class UserPasswordChangeSerializer(serializers.Serializer):
    password = serializers.CharField(required=True, max_length=30)
    password1 = serializers.CharField(required=True, max_length=30)
    password2 = serializers.CharField(required=True, max_length=30)

    def validate(self, data):
        if not self.context['request'].user.check_password(data.get('password')):
            raise serializers.ValidationError({'old_password': 'Wrong password.'})
        if data.get('password1') != data.get('password2'):
            raise serializers.ValidationError({'password': 'Password must be confirmed correctly.'})
        return data

    def update(self, instance, validated_data):
        print(instance, type(instance))
        print(validated_data['password1'])
        instance.set_password(validated_data['password1'])
        instance.save()
        return instance

    def create(self, validated_data):
        pass

    # @property
    # def data(self):
    #     return {'Success': True}
