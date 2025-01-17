# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .i18n import I18n
from .leave_subtype import LeaveSubtype


class LeaveType(object):
    _types = {
        "leave_type_id": str,
        "leave_type_name": List[I18n],
        "status": int,
        "leave_subtype_list": List[LeaveSubtype],
        "created_at": str,
        "created_by": str,
        "updated_at": str,
        "updated_by": str,
    }

    def __init__(self, d=None):
        self.leave_type_id: Optional[str] = None
        self.leave_type_name: Optional[List[I18n]] = None
        self.status: Optional[int] = None
        self.leave_subtype_list: Optional[List[LeaveSubtype]] = None
        self.created_at: Optional[str] = None
        self.created_by: Optional[str] = None
        self.updated_at: Optional[str] = None
        self.updated_by: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LeaveTypeBuilder":
        return LeaveTypeBuilder()


class LeaveTypeBuilder(object):
    def __init__(self) -> None:
        self._leave_type = LeaveType()

    def leave_type_id(self, leave_type_id: str) -> "LeaveTypeBuilder":
        self._leave_type.leave_type_id = leave_type_id
        return self

    def leave_type_name(self, leave_type_name: List[I18n]) -> "LeaveTypeBuilder":
        self._leave_type.leave_type_name = leave_type_name
        return self

    def status(self, status: int) -> "LeaveTypeBuilder":
        self._leave_type.status = status
        return self

    def leave_subtype_list(self, leave_subtype_list: List[LeaveSubtype]) -> "LeaveTypeBuilder":
        self._leave_type.leave_subtype_list = leave_subtype_list
        return self

    def created_at(self, created_at: str) -> "LeaveTypeBuilder":
        self._leave_type.created_at = created_at
        return self

    def created_by(self, created_by: str) -> "LeaveTypeBuilder":
        self._leave_type.created_by = created_by
        return self

    def updated_at(self, updated_at: str) -> "LeaveTypeBuilder":
        self._leave_type.updated_at = updated_at
        return self

    def updated_by(self, updated_by: str) -> "LeaveTypeBuilder":
        self._leave_type.updated_by = updated_by
        return self

    def build(self) -> "LeaveType":
        return self._leave_type
