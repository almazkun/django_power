from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView
from myauth.forms import (
    MyUserCreationForm,
    MyPasswordChangeForm,
    MyUserDeleteForm,
    MyAuthenticationForm,
)
from myauth.services import create_token_for_user
from django.contrib.auth.models import User
from django.contrib import messages

class HomeView(TemplateView):
    template_name = "home.html"


class MyFormView(FormView):
    success_url = reverse_lazy("home_user")
    success_context = dict()
    msg = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["success"] = self.success_context
        return context
    
    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, f'Success: {user.email}')
        return super().form_valid(form)


class UserCreateView(MyFormView):
    template_name = "user_create.html"
    form_class = MyUserCreationForm
    msg = messages.success


class UserUpdateView(MyFormView):
    template_name = "user_update.html"
    form_class = MyPasswordChangeForm
    msg = messages.info


class UserDeleteView(MyFormView):
    template_name = "user_delete.html"
    form_class = MyUserDeleteForm
    msg = messages.warning


class UserGetToken(MyFormView):
    template_name = "user_get_token.html"
    form_class = MyAuthenticationForm
    success_url = reverse_lazy("get_user_token")

    def form_valid(self, form):
        user = form.save(commit=False)
        self.success_context["token"] = user.token.token
        return super().form_valid(form)

