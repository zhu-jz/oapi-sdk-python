# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .okr import Okr


class OkrListInfo(object):
    _types = {
        "current_okr": Okr,
        "okr_list": List[Okr],
    }

    def __init__(self, d=None):
        self.current_okr: Optional[Okr] = None
        self.okr_list: Optional[List[Okr]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OkrListInfoBuilder":
        return OkrListInfoBuilder()


class OkrListInfoBuilder(object):
    def __init__(self) -> None:
        self._okr_list_info = OkrListInfo()

    def current_okr(self, current_okr: Okr) -> "OkrListInfoBuilder":
        self._okr_list_info.current_okr = current_okr
        return self

    def okr_list(self, okr_list: List[Okr]) -> "OkrListInfoBuilder":
        self._okr_list_info.okr_list = okr_list
        return self

    def build(self) -> "OkrListInfo":
        return self._okr_list_info
