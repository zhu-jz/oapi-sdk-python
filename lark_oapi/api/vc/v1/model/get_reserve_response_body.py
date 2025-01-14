# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .reserve import Reserve


class GetReserveResponseBody(object):
    _types = {
        "reserve": Reserve,
    }

    def __init__(self, d=None):
        self.reserve: Optional[Reserve] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetReserveResponseBodyBuilder":
        return GetReserveResponseBodyBuilder()


class GetReserveResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_reserve_response_body = GetReserveResponseBody()

    def reserve(self, reserve: Reserve) -> "GetReserveResponseBodyBuilder":
        self._get_reserve_response_body.reserve = reserve
        return self

    def build(self) -> "GetReserveResponseBody":
        return self._get_reserve_response_body
