from django.urls import path, re_path
from users_api.views import UserRUD, UserCreate, TokenDelete, VerificationView
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'users_api'

urlpatterns = [
    path('token/', obtain_auth_token, name='token'),
    path('token/delete/', TokenDelete.as_view(), name='TokenDelete'),
    path('user-rud/<email>/', UserRUD.as_view(), name='UserRUD'),
    path('user-create/', UserCreate.as_view(), name='UserCreate'),
    path('activate/<uidb64>/<token>/', VerificationView.as_view(), name='activate'),
]
