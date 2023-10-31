# mypy: ignore-errors
from django.db import models


class TimeStampMixIn(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
