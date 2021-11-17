from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"


class UserCreateView(TemplateView):
    template_name = "user_create.html"


class UserUpdateView(TemplateView):
    template_name = "user_update.html"


class UserDeleteView(TemplateView):
    template_name = "user_delete.html"


class UserIsValidToken(TemplateView):
    template_name = "user_is_valid_token.html"


class UserGetToken(TemplateView):
    template_name = "user_get_token.html"
