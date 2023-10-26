# mypy: ignore-errors
from django.db import models


class User(models.Model):
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.IntegerField()


class Role(models.Model):
    value = models.CharField(max_length=15)


class Issues(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    junior_id = models.IntegerField
    senior_id = models.IntegerField(null=True)
    status = models.CharField(max_length=10)
