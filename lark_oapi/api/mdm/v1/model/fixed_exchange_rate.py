# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class FixedExchangeRate(object):
    _types = {
        "source_currency": str,
        "target_currency": str,
        "effective_date": str,
        "exchange_rate": str,
        "status": int,
    }

    def __init__(self, d=None):
        self.source_currency: Optional[str] = None
        self.target_currency: Optional[str] = None
        self.effective_date: Optional[str] = None
        self.exchange_rate: Optional[str] = None
        self.status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FixedExchangeRateBuilder":
        return FixedExchangeRateBuilder()


class FixedExchangeRateBuilder(object):
    def __init__(self) -> None:
        self._fixed_exchange_rate = FixedExchangeRate()

    def source_currency(self, source_currency: str) -> "FixedExchangeRateBuilder":
        self._fixed_exchange_rate.source_currency = source_currency
        return self

    def target_currency(self, target_currency: str) -> "FixedExchangeRateBuilder":
        self._fixed_exchange_rate.target_currency = target_currency
        return self

    def effective_date(self, effective_date: str) -> "FixedExchangeRateBuilder":
        self._fixed_exchange_rate.effective_date = effective_date
        return self

    def exchange_rate(self, exchange_rate: str) -> "FixedExchangeRateBuilder":
        self._fixed_exchange_rate.exchange_rate = exchange_rate
        return self

    def status(self, status: int) -> "FixedExchangeRateBuilder":
        self._fixed_exchange_rate.status = status
        return self

    def build(self) -> "FixedExchangeRate":
        return self._fixed_exchange_rate
