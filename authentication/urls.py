from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from authentication import views


urlpatterns = [
    path('register', views.RegisterAPIView.as_view(), name='register'),
    path('login', views.LoginAPIView.as_view(), name='login'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/token_verify', TokenVerifyView.as_view(), name='token_verify'),
]
