# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .reserve_callee import ReserveCallee


class ReserveCallSetting(object):
    _types = {
        "callee": ReserveCallee,
    }

    def __init__(self, d=None):
        self.callee: Optional[ReserveCallee] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReserveCallSettingBuilder":
        return ReserveCallSettingBuilder()


class ReserveCallSettingBuilder(object):
    def __init__(self) -> None:
        self._reserve_call_setting = ReserveCallSetting()

    def callee(self, callee: ReserveCallee) -> "ReserveCallSettingBuilder":
        self._reserve_call_setting.callee = callee
        return self

    def build(self) -> "ReserveCallSetting":
        return self._reserve_call_setting
