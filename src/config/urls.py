from django.contrib import admin
from django.urls import path
from .exchange_rates import exchange_rates

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('exchange-rates/', exchange_rates),
]


