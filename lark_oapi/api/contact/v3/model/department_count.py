# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class DepartmentCount(object):
    _types = {
        "department_id": int,
        "direct_department_count": int,
        "direct_user_count": int,
        "department_count": int,
        "user_count": int,
    }

    def __init__(self, d=None):
        self.department_id: Optional[int] = None
        self.direct_department_count: Optional[int] = None
        self.direct_user_count: Optional[int] = None
        self.department_count: Optional[int] = None
        self.user_count: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DepartmentCountBuilder":
        return DepartmentCountBuilder()


class DepartmentCountBuilder(object):
    def __init__(self) -> None:
        self._department_count = DepartmentCount()

    def department_id(self, department_id: int) -> "DepartmentCountBuilder":
        self._department_count.department_id = department_id
        return self

    def direct_department_count(self, direct_department_count: int) -> "DepartmentCountBuilder":
        self._department_count.direct_department_count = direct_department_count
        return self

    def direct_user_count(self, direct_user_count: int) -> "DepartmentCountBuilder":
        self._department_count.direct_user_count = direct_user_count
        return self

    def department_count(self, department_count: int) -> "DepartmentCountBuilder":
        self._department_count.department_count = department_count
        return self

    def user_count(self, user_count: int) -> "DepartmentCountBuilder":
        self._department_count.user_count = user_count
        return self

    def build(self) -> "DepartmentCount":
        return self._department_count
