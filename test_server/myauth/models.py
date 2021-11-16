from django.db import models
from django.contrib.auth.models import User
from secrets import token_urlsafe


# Create your models here.
def create_unique_token():
    while True:
        token = token_urlsafe(256)[:255]
        if not Token.objects.filter(token=token).exists():
            return token


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, default=create_unique_token)
    created = models.DateTimeField(auto_now_add=True)
