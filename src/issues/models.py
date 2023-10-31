# mypy: ignore-errors
from django.db import models

from shared.django import TimeStampMixIn


class Issue(TimeStampMixIn):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=255)
    status = models.CharField(max_length=10)
    junior_id = models.IntegerField
    senior_id = models.IntegerField(null=True)

    class Meta:
        db_table = "issues"


class Message(TimeStampMixIn):
    content = models.CharField(max_length=100)
    author_id = models.IntegerField()
    issue_id = models.IntegerField()

    class Meta:
        db_table = "issues_messages"
