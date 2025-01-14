# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .department_i18n_name import DepartmentI18nName
from .department_leader import DepartmentLeader
from .department_status import DepartmentStatus


class Department(object):
    _types = {
        "name": str,
        "i18n_name": DepartmentI18nName,
        "parent_department_id": str,
        "department_id": str,
        "open_department_id": str,
        "leader_user_id": str,
        "chat_id": str,
        "order": int,
        "unit_ids": List[str],
        "member_count": int,
        "status": DepartmentStatus,
        "create_group_chat": bool,
        "leaders": List[DepartmentLeader],
        "group_chat_employee_types": List[int],
        "department_hrbps": List[str],
        "primary_member_count": int,
    }

    def __init__(self, d=None):
        self.name: Optional[str] = None
        self.i18n_name: Optional[DepartmentI18nName] = None
        self.parent_department_id: Optional[str] = None
        self.department_id: Optional[str] = None
        self.open_department_id: Optional[str] = None
        self.leader_user_id: Optional[str] = None
        self.chat_id: Optional[str] = None
        self.order: Optional[int] = None
        self.unit_ids: Optional[List[str]] = None
        self.member_count: Optional[int] = None
        self.status: Optional[DepartmentStatus] = None
        self.create_group_chat: Optional[bool] = None
        self.leaders: Optional[List[DepartmentLeader]] = None
        self.group_chat_employee_types: Optional[List[int]] = None
        self.department_hrbps: Optional[List[str]] = None
        self.primary_member_count: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DepartmentBuilder":
        return DepartmentBuilder()


class DepartmentBuilder(object):
    def __init__(self) -> None:
        self._department = Department()

    def name(self, name: str) -> "DepartmentBuilder":
        self._department.name = name
        return self

    def i18n_name(self, i18n_name: DepartmentI18nName) -> "DepartmentBuilder":
        self._department.i18n_name = i18n_name
        return self

    def parent_department_id(self, parent_department_id: str) -> "DepartmentBuilder":
        self._department.parent_department_id = parent_department_id
        return self

    def department_id(self, department_id: str) -> "DepartmentBuilder":
        self._department.department_id = department_id
        return self

    def open_department_id(self, open_department_id: str) -> "DepartmentBuilder":
        self._department.open_department_id = open_department_id
        return self

    def leader_user_id(self, leader_user_id: str) -> "DepartmentBuilder":
        self._department.leader_user_id = leader_user_id
        return self

    def chat_id(self, chat_id: str) -> "DepartmentBuilder":
        self._department.chat_id = chat_id
        return self

    def order(self, order: int) -> "DepartmentBuilder":
        self._department.order = order
        return self

    def unit_ids(self, unit_ids: List[str]) -> "DepartmentBuilder":
        self._department.unit_ids = unit_ids
        return self

    def member_count(self, member_count: int) -> "DepartmentBuilder":
        self._department.member_count = member_count
        return self

    def status(self, status: DepartmentStatus) -> "DepartmentBuilder":
        self._department.status = status
        return self

    def create_group_chat(self, create_group_chat: bool) -> "DepartmentBuilder":
        self._department.create_group_chat = create_group_chat
        return self

    def leaders(self, leaders: List[DepartmentLeader]) -> "DepartmentBuilder":
        self._department.leaders = leaders
        return self

    def group_chat_employee_types(self, group_chat_employee_types: List[int]) -> "DepartmentBuilder":
        self._department.group_chat_employee_types = group_chat_employee_types
        return self

    def department_hrbps(self, department_hrbps: List[str]) -> "DepartmentBuilder":
        self._department.department_hrbps = department_hrbps
        return self

    def primary_member_count(self, primary_member_count: int) -> "DepartmentBuilder":
        self._department.primary_member_count = primary_member_count
        return self

    def build(self) -> "Department":
        return self._department
