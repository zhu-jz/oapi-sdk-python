# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .subscribe_user import SubscribeUser


class ReserveFormConfig(object):
    _types = {
        "reserve_form": bool,
        "notified_users": List[SubscribeUser],
        "notified_time": int,
        "time_unit": int,
    }

    def __init__(self, d=None):
        self.reserve_form: Optional[bool] = None
        self.notified_users: Optional[List[SubscribeUser]] = None
        self.notified_time: Optional[int] = None
        self.time_unit: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReserveFormConfigBuilder":
        return ReserveFormConfigBuilder()


class ReserveFormConfigBuilder(object):
    def __init__(self) -> None:
        self._reserve_form_config = ReserveFormConfig()

    def reserve_form(self, reserve_form: bool) -> "ReserveFormConfigBuilder":
        self._reserve_form_config.reserve_form = reserve_form
        return self

    def notified_users(self, notified_users: List[SubscribeUser]) -> "ReserveFormConfigBuilder":
        self._reserve_form_config.notified_users = notified_users
        return self

    def notified_time(self, notified_time: int) -> "ReserveFormConfigBuilder":
        self._reserve_form_config.notified_time = notified_time
        return self

    def time_unit(self, time_unit: int) -> "ReserveFormConfigBuilder":
        self._reserve_form_config.time_unit = time_unit
        return self

    def build(self) -> "ReserveFormConfig":
        return self._reserve_form_config
