from django.contrib.auth.forms import UserCreationForm
from myauth.services import (
    validate_email,
    create_token_for_user,
    get_user_by_email_and_pass,
)
from myauth.services import generate_unique_username
from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core import validators


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email", max_length=254)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True
        self.fields = {
            "email": self.fields["email"],
            "password1": self.fields["password1"],
            "password2": self.fields["password2"],
        }

    def clean(self):
        validate_email(self.cleaned_data.get("email"))
        self.cleaned_data["username"] = generate_unique_username()
        return super().clean()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.save()
        return super().save()


class MyAuthenticationForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        self.user_ = get_user_by_email_and_pass(
            self.cleaned_data.get("email"), self.cleaned_data.get("password")
        )
        return super().clean()

    def save(self, commit=True):
        if commit:
            self.user_.save()
        return self.user_


class MyPasswordChangeForm(MyAuthenticationForm):
    new_password = forms.CharField(
        widget=forms.PasswordInput, validators=[validate_password], required=True
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["new_password"])
        user.save()
        return user


class MyUserDeleteForm(MyAuthenticationForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        user.delete()
        return user

