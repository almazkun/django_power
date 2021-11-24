from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from myauth.forms import (
    MyAuthenticationForm,
    MyPasswordChangeForm,
    MyUserCreationForm,
    MyUserDeleteForm,
)

from myauth.services import validate_token


class HomeView(TemplateView):
    template_name = "home.html"


class MyFormView(FormView):
    success_url = reverse_lazy("home_user")
    success_message = ""

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        success_message = self.get_success_message(user)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, user) -> str:
        if user is None:
            return self.success_message
        return self.success_message % {
            "email": user.email,
            "token": user.token.token,
        }


class UserCreateView(MyFormView):
    template_name = "user_create.html"
    form_class = MyUserCreationForm
    success_message = "New User created: %(email)s!"


class UserUpdateView(MyFormView):
    template_name = "user_update.html"
    form_class = MyPasswordChangeForm
    success_message = "Password updated: %(email)s!"


class UserDeleteView(MyFormView):
    template_name = "user_delete.html"
    form_class = MyUserDeleteForm
    success_message = "User deleted!"


class UserGetToken(MyFormView):
    template_name = "user_get_token.html"
    form_class = MyAuthenticationForm
    success_message = "Your token: %(token)s"


class UserValidateToken(TemplateView):
    template_name = "user_validate_token.html"

    def get(self, request, *args, **kwargs):
        token = request.GET.get("token")
        if token:
            valid = validate_token(token)
            if valid:
                messages.success(request, "Token is valid!")
            else:
                messages.error(request, "Token is NOT valid!")
        return super().get(request, *args, **kwargs)