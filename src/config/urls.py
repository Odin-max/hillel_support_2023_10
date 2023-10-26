# mypy: ignore-errors
from django.urls import path

from users import api

from .exchange_rates import exchange_rate_history, exchange_rates

urlpatterns = [
    path("exchange-rates/", exchange_rates, name="exchange_rates"),
    path(
        "exchange-rates/history/",
        exchange_rate_history,
        name="exchange_rate_history",
    ),
    path("users/all", api.all),
    path("users/create", api.create),
    path("users/issues/create", api.create_issue),
    path("users/issues/get", api.get_issues),
]
