# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .user_okr_objective import UserOkrObjective


class UserOkr(object):
    _types = {
        "id": int,
        "name": str,
        "permission": int,
        "objective_list": List[UserOkrObjective],
    }

    def __init__(self, d=None):
        self.id: Optional[int] = None
        self.name: Optional[str] = None
        self.permission: Optional[int] = None
        self.objective_list: Optional[List[UserOkrObjective]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserOkrBuilder":
        return UserOkrBuilder()


class UserOkrBuilder(object):
    def __init__(self) -> None:
        self._user_okr = UserOkr()

    def id(self, id: int) -> "UserOkrBuilder":
        self._user_okr.id = id
        return self

    def name(self, name: str) -> "UserOkrBuilder":
        self._user_okr.name = name
        return self

    def permission(self, permission: int) -> "UserOkrBuilder":
        self._user_okr.permission = permission
        return self

    def objective_list(self, objective_list: List[UserOkrObjective]) -> "UserOkrBuilder":
        self._user_okr.objective_list = objective_list
        return self

    def build(self) -> "UserOkr":
        return self._user_okr
