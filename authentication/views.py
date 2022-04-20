from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from authentication.serializers import RegisterSerializer, LogInSerializer
from rest_framework import response, status
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BaseAuthentication


class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(TokenObtainPairView):
    serializer_class = LogInSerializer


class UserViewAPI(BaseAuthentication):
    ...