from django.urls import path
from rest_framework.routers import DefaultRouter

from .api import IssueApiSet, MessageCreateAPI

router = DefaultRouter()
router.register("", IssueApiSet, basename="issues")
# urlpatterns = router.urls


messages_urls = [
    path("<int:issue_id>/messages/create/", MessageCreateAPI.as_view())

]

urlpatterns = router.urls + messages_urls