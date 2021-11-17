from django.test import Client, TestCase
from django.urls import reverse

from .models import create_unique_token


# Create your tests here.
class TestModels(TestCase):
    def test_create_unique_token(self):
        token = create_unique_token()

        self.assertEqual(len(token), 255)


class TesstViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_create_view(self):
        response = self.client.get(reverse("create_user"))
        response.status_code = 200

    def test_user_update_view(self):
        response = self.client.get(reverse("update_user"))
        response.status_code = 200

    def test_user_delete_view(self):
        response = self.client.get(reverse("delete_user"))
        response.status_code = 200

    def test_user_is_valid_token_view(self):
        response = self.client.get(reverse("is_valid_token"))
        response.status_code = 200

    def test_user_get_token_view(self):
        response = self.client.get(reverse("get_token"))
        response.status_code = 200
