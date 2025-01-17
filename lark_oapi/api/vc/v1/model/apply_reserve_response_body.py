# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .reserve import Reserve
from .reserve_correction_check_info import ReserveCorrectionCheckInfo


class ApplyReserveResponseBody(object):
    _types = {
        "reserve": Reserve,
        "reserve_correction_check_info": ReserveCorrectionCheckInfo,
    }

    def __init__(self, d=None):
        self.reserve: Optional[Reserve] = None
        self.reserve_correction_check_info: Optional[ReserveCorrectionCheckInfo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApplyReserveResponseBodyBuilder":
        return ApplyReserveResponseBodyBuilder()


class ApplyReserveResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._apply_reserve_response_body = ApplyReserveResponseBody()

    def reserve(self, reserve: Reserve) -> "ApplyReserveResponseBodyBuilder":
        self._apply_reserve_response_body.reserve = reserve
        return self

    def reserve_correction_check_info(self,
                                      reserve_correction_check_info: ReserveCorrectionCheckInfo) -> "ApplyReserveResponseBodyBuilder":
        self._apply_reserve_response_body.reserve_correction_check_info = reserve_correction_check_info
        return self

    def build(self) -> "ApplyReserveResponseBody":
        return self._apply_reserve_response_body
