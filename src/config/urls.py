# mypy: ignore-errors
from django.urls import path

from .exchange_rates import exchange_rate_history, exchange_rates

urlpatterns = [
    path("exchange-rates/", exchange_rates, name="exchange_rates"),
    path(
        "exchange-rates/history/",
        exchange_rate_history,
        name="exchange_rate_history",
    ),
]
