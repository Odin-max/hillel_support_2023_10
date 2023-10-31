# mypy: ignore-errors
from django.db import models


class Role(models.Model):
    value = models.CharField(max_length=15)


class User(models.Model):
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.IntegerField()
