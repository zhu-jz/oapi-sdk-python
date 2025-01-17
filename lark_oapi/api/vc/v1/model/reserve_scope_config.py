# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .subscribe_department import SubscribeDepartment
from .subscribe_user import SubscribeUser


class ReserveScopeConfig(object):
    _types = {
        "allow_all_users": int,
        "allow_users": List[SubscribeUser],
        "allow_depts": List[SubscribeDepartment],
    }

    def __init__(self, d=None):
        self.allow_all_users: Optional[int] = None
        self.allow_users: Optional[List[SubscribeUser]] = None
        self.allow_depts: Optional[List[SubscribeDepartment]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReserveScopeConfigBuilder":
        return ReserveScopeConfigBuilder()


class ReserveScopeConfigBuilder(object):
    def __init__(self) -> None:
        self._reserve_scope_config = ReserveScopeConfig()

    def allow_all_users(self, allow_all_users: int) -> "ReserveScopeConfigBuilder":
        self._reserve_scope_config.allow_all_users = allow_all_users
        return self

    def allow_users(self, allow_users: List[SubscribeUser]) -> "ReserveScopeConfigBuilder":
        self._reserve_scope_config.allow_users = allow_users
        return self

    def allow_depts(self, allow_depts: List[SubscribeDepartment]) -> "ReserveScopeConfigBuilder":
        self._reserve_scope_config.allow_depts = allow_depts
        return self

    def build(self) -> "ReserveScopeConfig":
        return self._reserve_scope_config
