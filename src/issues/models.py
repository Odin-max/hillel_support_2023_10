# mypy: ignore-errors
from django.conf import settings
from django.db import models

from shared.django import TimeStampMixIn


class Issue(TimeStampMixIn):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=255)
    status = models.CharField(max_length=10)

    junior = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="junior_issues",
    )
    senior = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="senior_issues",
    )

    class Meta:
        db_table = "issues"


class Message(TimeStampMixIn):
    content = models.CharField(max_length=100)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="messages",
    )
    issue = models.ForeignKey(
        "issues.Issue", on_delete=models.DO_NOTHING, related_name="messages"
    )

    class Meta:
        db_table = "issues_messages"
