# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ReserveAssignHost(object):
    _types = {
        "user_type": int,
        "id": str,
    }

    def __init__(self, d=None):
        self.user_type: Optional[int] = None
        self.id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReserveAssignHostBuilder":
        return ReserveAssignHostBuilder()


class ReserveAssignHostBuilder(object):
    def __init__(self) -> None:
        self._reserve_assign_host = ReserveAssignHost()

    def user_type(self, user_type: int) -> "ReserveAssignHostBuilder":
        self._reserve_assign_host.user_type = user_type
        return self

    def id(self, id: str) -> "ReserveAssignHostBuilder":
        self._reserve_assign_host.id = id
        return self

    def build(self) -> "ReserveAssignHost":
        return self._reserve_assign_host
