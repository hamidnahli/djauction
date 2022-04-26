from django.urls import path
from account.views import RetrieveUserProfile, UpdateUserProfile

urlpatterns = [
    path('user/<int:user_id>/info', RetrieveUserProfile.as_view({'get': 'retrieve'}), name='profile'),
    path('user/update/<int:user_id>', UpdateUserProfile.as_view(), name='update_user'),
]
