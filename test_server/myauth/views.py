# is valid_user
# is valid_token
# new_user
# update_user
# delete_user
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.models import User

from django.views import View


class UserCreateView(CreateView):
    model = User
    template_name = "user_create.html"
    fields = ["email", "password"]


class UserUpdateView(UpdateView):
    model = User
    template_name = "user_update.html"
    fields = ["password"]


class UserDeleteView(DeleteView):
    model = User
    template_name = "user_delete.html"


class UserIsValidToken(View):
    def get(self, request, email):
        user = User.objects.filter(email=email)
        if user:
            return JsonResponse({"valid": True})
        else:
            return JsonResponse({"valid": False})


class UserGetToken(View):
    def get(self, request, email):
        user = User.objects.filter(email=email)
        if user:
            return JsonResponse({"token": user.token})
        else:
            return JsonResponse({"token": None})
