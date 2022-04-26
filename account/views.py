from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import UpdateAPIView
from authentication.models import User
from account.serializers import RetrieveUserProfileSerializer, UpdateUserProfileSerializer


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


