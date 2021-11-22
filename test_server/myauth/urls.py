from django.urls import path
from myauth.views import (
    HomeView,
    UserCreateView,
    UserDeleteView,
    UserGetToken,
    UserUpdateView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home_user"),
    path("create/", UserCreateView.as_view(), name="create_user"),
    path("update/", UserUpdateView.as_view(), name="update_user"),
    path("delete/", UserDeleteView.as_view(), name="delete_user"),
    path("token/", UserGetToken.as_view(), name="get_user_token"),
]
