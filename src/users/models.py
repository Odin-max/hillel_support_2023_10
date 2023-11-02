# mypy: ignore-errors
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from .constants import Role
from .managers import UserManager


class User(AbstractUser, PermissionsMixin):
    email = models.CharField(max_length=40, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    is_staff = models.BooleanField(default=False)
    is_active = (models.BooleanField(default=True),)

    role = models.CharField(
        max_length=2, default=Role.JUNIOR, choices=Role.choices()
    )

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self) -> str:
        return self.first_name

    def __str__(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name}{self.last_name}"
        else:
            return self.email
