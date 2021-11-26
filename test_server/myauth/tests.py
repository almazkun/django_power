from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import Client, TestCase
from django.urls import reverse
from myauth.forms import (
    MyAuthenticationForm,
    MyPasswordChangeForm,
    MyUserCreationForm,
    MyUserDeleteForm,
)
from myauth.views import UserCreateView
from myauth.models import generate_unique_token
from myauth.services import generate_unique_username


# Create your tests here.
class TestModels(TestCase):
    def test_generate_unique_token(self):
        token = generate_unique_token()

        self.assertEqual(len(token), 255)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.post_data = {
            "email": "asd@asd.asd",
            "password1": "asdasdasd123",
            "password2": "asdasdasd123",
        }

    def test_user_create_view(self):
        response = self.client.get(reverse("create_user"))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], MyUserCreationForm)

        response = self.client.post(reverse("create_user"), self.post_data)
        user = User.objects.get(email=self.post_data.get("email"))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(user.email, self.post_data.get("email"))
        self.assertTrue(user.check_password(self.post_data.get("password1")))
        self.assertIsNotNone(user.token)

        response = self.client.post(reverse("create_user"), self.post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], MyUserCreationForm)
        self.assertFalse(response.context["form"].is_valid())

    def test_user_update_view(self):
        response = self.client.get(reverse("update_user"))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], MyPasswordChangeForm)

        self.client.post(reverse("create_user"), self.post_data)
        new_password = "cxzdsaewq321"

        response = self.client.post(
            reverse("update_user"),
            {
                "email": self.post_data.get("email"),
                "password": self.post_data.get("password1"),
                "new_password": new_password,
            },
        )
        user = User.objects.get(email=self.post_data.get("email"))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(user.email, self.post_data.get("email"))
        self.assertTrue(user.check_password(new_password))

    def test_user_delete_view(self):
        response = self.client.get(reverse("delete_user"))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], MyUserDeleteForm)

        self.client.post(reverse("create_user"), self.post_data)

        response = self.client.post(
            reverse("delete_user"),
            {
                "email": self.post_data.get("email"),
                "password": self.post_data.get("password1"),
            },
        )

        self.assertEqual(response.status_code, 302)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(email=self.post_data.get("email"))

    def test_user_get_token_view(self):
        response = self.client.get(reverse("get_user_token"))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], MyAuthenticationForm)

        self.client.post(reverse("create_user"), self.post_data)
        user = User.objects.get(email=self.post_data.get("email"))

        response = self.client.post(
            reverse("get_user_token"),
            {
                "email": self.post_data.get("email"),
                "password": self.post_data.get("password1"),
            },
        )

        self.assertEqual(response.status_code, 302)

    def test_validate_token(self):
        self.client.post(reverse("create_user"), self.post_data)
        user = User.objects.get(email=self.post_data.get("email"))

        response = self.client.get(
            reverse("validate_user_token"), data={"token": user.token.token}
        )
        self.assertTrue(
            any(
                [
                    "Token is valid!" in message.message
                    for message in response.context["messages"]
                ]
            )
        )

        response = self.client.get(
            reverse("validate_user_token"), data={"token": "user.token.token"}
        )
        self.assertTrue(
            any(
                [
                    "Token is NOT valid!" in message.message
                    for message in response.context["messages"]
                ]
            )
        )


class TestForms(TestCase):
    def test_my_authentication_form(self):
        username = "username"
        data = {
            "email": "asd@asd.asd",
            "password": "asdasdasd123",
        }

        form = MyAuthenticationForm(data=data)
        self.assertFalse(form.is_valid())
        with self.assertRaises(ValidationError):
            form.clean()

        user = User.objects.create_user(username, **data)
        form = MyAuthenticationForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.save(), user)

        data["password"] = "asdasdasd"
        form = MyAuthenticationForm(data=data)
        self.assertFalse(form.is_valid())
        with self.assertRaises(ValidationError):
            form.clean()


class TestServices(TestCase):
    def test_generate_unique_username(self):
        username = generate_unique_username()

        self.assertEqual(len(username), 150)
