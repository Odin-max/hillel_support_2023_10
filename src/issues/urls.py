# mypy: ignore-errors
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api import IssueApiSet, MessageCreateAPI, MessageList

router = DefaultRouter()
router.register("", IssueApiSet, basename="issues")
# urlpatterns = router.urls


messages_urls = [
    path("<int:issue_id>/messages/create/", MessageCreateAPI.as_view(), name="message-create"),  # Add name for easier referencing
    path("issues/<int:issue_id>/messages/", MessageList.as_view(), name="message-list"),  # Add the new endpoint for listing messages
]

urlpatterns = [
    *router.urls,  
    path("", include(messages_urls)),  
]
    # router.urls + messages_urls
