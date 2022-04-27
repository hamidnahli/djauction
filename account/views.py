from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import UpdateAPIView
from authentication.models import User
from account.serializers import RetrieveUserProfileSerializer, UpdateUserProfileSerializer, UserPasswordChangeSerializer


class RetrieveUserProfile(viewsets.ModelViewSet):
    lookup_field = 'pk'
    lookup_url_kwarg = 'user_id'
    permission_classes = (IsAuthenticated,)
    serializer_class = RetrieveUserProfileSerializer

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)


class UpdateUserProfile(UpdateAPIView):
    lookup_field = 'pk'
    lookup_url_kwarg = 'user_id'
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserProfileSerializer

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)


class APIChangePasswordView(UpdateAPIView):
    lookup_field = 'pk'
    lookup_url_kwarg = 'user_id'
    serializer_class = UserPasswordChangeSerializer
    model = get_user_model()
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)
