from django.test import TestCase
from .models import create_unique_token

# Create your tests here.
class TestModels(TestCase):
    def test_create_unique_token(self):
        token = create_unique_token()

        self.assertEqual(len(token), 255)