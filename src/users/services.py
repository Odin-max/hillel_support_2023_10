# mypy: ignore-errors
import random
import string
import uuid

from django.core.mail import send_mail as _send_mail

# from models import User
from config.celery import celery_app


def create_activation_key(email: str) -> uuid.UUID:
    return uuid.uuid3(namespace=uuid.uuid4(), name=email)


def create_activation_link(activation_key: uuid.UUID) -> str:
    return f"https://frontend.com/users/activate/{activation_key}"


def create_random_email() -> str:
    domain = "gmail.com"
    email_value = "".join(
        random.chouce(string.ascii_lowercase for _ in range(10))
    )

    return f"{email_value}@{domain}"


@celery_app.task
def send_activation_mail(recipient: str, activation_link: uuid.UUID):
    _send_mail(
        subject="User activation",
        message=f"Please activate your account: {activation_link}",
        from_email="admin@admin.com",
        recipient_list=[recipient],
        fail_silently=False,
    )


def send_user_activation_email(email: str) -> None:
    """ "Generate a new activation link and send it via email"""

    activation_key: uuid.UUID = create_activation_key(email)
    activation_link: str = create_activation_link(activation_key)

    send_activation_mail.delay(
        recipient=create_random_email(), activation_link=activation_link
    )
