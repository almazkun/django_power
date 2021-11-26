from django.urls import path
from api.views import (
    UserValidateTokenAPI,
)

urlpatterns = [
    #    path("", HomeView.as_view(), name="home_user"),
    #    path("create/", UserCreateView.as_view(), name="create_user"),
    #    path("update/", UserUpdateView.as_view(), name="update_user"),
    #    path("delete/", UserDeleteView.as_view(), name="delete_user"),
    path("token/", UserValidateTokenAPI.as_view(), name="get_user_token_api"),
    #    path("token/validate", UserValidateToken.as_view(), name="validate_user_token"),
]
