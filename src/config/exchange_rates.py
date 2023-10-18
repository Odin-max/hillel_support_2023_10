import requests  # type: ignore
from django.http import JsonResponse  # type: ignore
from pydantic import BaseModel, Field

API_KEY = "HDKIKI6WAC2J677G"
BASE_URL = "https://www.alphavantage.co"


class AlphavantageCurrencyExchangeRatesRequest(BaseModel):
    currency_from: str
    currency_to: str


class AlphavantageCurrencyExchangeRatesResults(BaseModel):
    currency_from: str = Field(alias="1. From_Currency Code")
    currency_to: str = Field(alias="3. To_Currency Code")
    rate: float = Field(alias="5. Exchange Rate")


class AlphavantageCurrencyExchangeRatesResponse(BaseModel):
    results: AlphavantageCurrencyExchangeRatesResults = Field(
        alias="Realtime Currency Exchange Rate"
    )


def fetch_currency_exchange_rates(
    schema: AlphavantageCurrencyExchangeRatesRequest,
) -> AlphavantageCurrencyExchangeRatesResponse:
    """This function claims the currency exchange rate information
    from the external service: Alphavantage.
    """

    payload: str = (
        "/query?function=CURRENCY_EXCHANGE_RATE&"
        f"from_currency={schema.currency_from.upper()}&"
        f"to_currency={schema.currency_to.upper()}&"
        f"apikey={API_KEY}"
    )
    url: str = "".join([BASE_URL, payload])

    raw_response: requests.Response = requests.get(url)
    response = AlphavantageCurrencyExchangeRatesResponse(**raw_response.json())

    return response


def exchange_rates(request) -> JsonResponse:
    currency_from = request.GET.get("currency_from", "usd")
    currency_to = request.GET.get("currency_to", "uah")
    result: AlphavantageCurrencyExchangeRatesResponse = (
        fetch_currency_exchange_rates(
            schema=AlphavantageCurrencyExchangeRatesRequest(
                currency_from=currency_from, currency_to=currency_to
            )
        )
    )

    headers: dict = {
        # "Content-Type": "application/json", # for http response
        "Access-Control-Allow-Origin": "*",
    }

    return JsonResponse(data=result.model_dump(), headers=headers)
