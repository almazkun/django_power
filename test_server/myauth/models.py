from django.db import models
from django.contrib.auth.models import User
from secrets import token_urlsafe
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
def generate_unique_token():
    while True:
        token = token_urlsafe(256)[:255]
        if not Token.objects.filter(token=token).exists():
            return token


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="token")
    token = models.CharField(max_length=255, default=generate_unique_token)
    created = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=User)
def create_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
