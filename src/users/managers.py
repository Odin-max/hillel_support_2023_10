# mypy: ignore-errors
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager

from .constants import Role


class UserManager(BaseUserManager):
    def _create_user(
        self, email: str, password: str | None = None, **extra_fields
    ):
        email = self.normalize_email(email=email)
        user = self.model(
            email=self.normalize_email(email=email), **extra_fields
        )
        setattr(user, "password", make_password(password=password))
        user.save(using=self._db)

        return user

    def create_user(
        self, email: str, password: str | None = None, **extra_fields
    ):
        extra_fields["is_staff"] = False
        extra_fields["is_superuser"] = False
        extra_fields["role"] = Role.JUNIOR

        return self._create_user(email, password, **extra_fields)

    def create_superuser(
        self, email: str, password: str | None = None, **extra_fields
    ):
        extra_fields["is_staff"] = True
        extra_fields["is_superuser"] = True
        extra_fields["role"] = Role.ADMIN

        return self._create_user(email, password, **extra_fields)
