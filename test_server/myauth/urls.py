from django.urls import path


from myauth.views import (
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
    UserIsValidToken,
    UserGetToken,
)


urlpatterns = [
    path("create/", UserCreateView.as_view(), name="create_user"),
    path("update/", UserUpdateView.as_view(), name="update_user"),
    path("delete/", UserDeleteView.as_view(), name="delete_user"),
    path("is_valid_token/", UserIsValidToken.as_view(), name="is_valid_token"),
    path("get_token/", UserGetToken.as_view(), name="get_token"),
]
