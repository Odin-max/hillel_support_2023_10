# mypy: ignore-errors
from django.urls import path

from .api import UserCreateAPI, UserRetrieveAPI

urlpatterns = [
    path("", UserCreateAPI.as_view()),
    path("", UserRetrieveAPI.as_view()),
]

# HTTP GET users/
# HTTP POST users/
