# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .enum import Enum


class ManageRelation(object):
    _types = {
        "subordinate_department_id": str,
        "subordinate_employee_id": str,
        "manager_type": Enum,
        "report_mode_type": Enum,
        "superior_employee_id": str,
        "effective_time": str,
    }

    def __init__(self, d=None):
        self.subordinate_department_id: Optional[str] = None
        self.subordinate_employee_id: Optional[str] = None
        self.manager_type: Optional[Enum] = None
        self.report_mode_type: Optional[Enum] = None
        self.superior_employee_id: Optional[str] = None
        self.effective_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ManageRelationBuilder":
        return ManageRelationBuilder()


class ManageRelationBuilder(object):
    def __init__(self) -> None:
        self._manage_relation = ManageRelation()

    def subordinate_department_id(self, subordinate_department_id: str) -> "ManageRelationBuilder":
        self._manage_relation.subordinate_department_id = subordinate_department_id
        return self

    def subordinate_employee_id(self, subordinate_employee_id: str) -> "ManageRelationBuilder":
        self._manage_relation.subordinate_employee_id = subordinate_employee_id
        return self

    def manager_type(self, manager_type: Enum) -> "ManageRelationBuilder":
        self._manage_relation.manager_type = manager_type
        return self

    def report_mode_type(self, report_mode_type: Enum) -> "ManageRelationBuilder":
        self._manage_relation.report_mode_type = report_mode_type
        return self

    def superior_employee_id(self, superior_employee_id: str) -> "ManageRelationBuilder":
        self._manage_relation.superior_employee_id = superior_employee_id
        return self

    def effective_time(self, effective_time: str) -> "ManageRelationBuilder":
        self._manage_relation.effective_time = effective_time
        return self

    def build(self) -> "ManageRelation":
        return self._manage_relation
