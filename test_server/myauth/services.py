from secrets import token_urlsafe

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from myauth.models import Token


def create_token_for_user(user: User) -> Token:
    return Token.objects.create(user=user)


def validate_email(email: str) -> None:
    if User.objects.filter(email=email).exists():
        raise ValidationError("Email already in use!")


def validate_token(token: str) -> bool:
    return Token.objects.filter(token=token).exists()


def generate_unique_username() -> str:
    while True:
        username = token_urlsafe(150)[:150]
        if not User.objects.filter(username=username).exists():
            return username


def get_user_by_email_and_pass(email: str, password: str) -> User:
    try:
        user = User.objects.get(email=email)
        if user.check_password(password):
            return user
        else:
            raise ValidationError("Password is incorrect")
    except (ValidationError, ObjectDoesNotExist):
        raise ValidationError("Email or password is incorrect!")
