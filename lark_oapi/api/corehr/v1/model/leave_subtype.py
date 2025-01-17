# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n


class LeaveSubtype(object):
    _types = {
        "leave_type_id": str,
        "leave_type_name": List[I18n],
    }

    def __init__(self, d=None):
        self.leave_type_id: Optional[str] = None
        self.leave_type_name: Optional[List[I18n]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LeaveSubtypeBuilder":
        return LeaveSubtypeBuilder()


class LeaveSubtypeBuilder(object):
    def __init__(self) -> None:
        self._leave_subtype = LeaveSubtype()

    def leave_type_id(self, leave_type_id: str) -> "LeaveSubtypeBuilder":
        self._leave_subtype.leave_type_id = leave_type_id
        return self

    def leave_type_name(self, leave_type_name: List[I18n]) -> "LeaveSubtypeBuilder":
        self._leave_subtype.leave_type_name = leave_type_name
        return self

    def build(self) -> "LeaveSubtype":
        return self._leave_subtype
