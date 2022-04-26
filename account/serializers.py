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

