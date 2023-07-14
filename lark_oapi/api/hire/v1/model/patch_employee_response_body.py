# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .employee import Employee


class PatchEmployeeResponseBody(object):
    _types = {
        "employee": Employee,
    }

    def __init__(self, d):
        self.employee: Optional[Employee] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchEmployeeResponseBodyBuilder":
        return PatchEmployeeResponseBodyBuilder()


class PatchEmployeeResponseBodyBuilder(object):
    def __init__(self, patch_employee_response_body: PatchEmployeeResponseBody = PatchEmployeeResponseBody({})) -> None:
        self._patch_employee_response_body: PatchEmployeeResponseBody = patch_employee_response_body
    
    def employee(self, employee: Employee) -> "PatchEmployeeResponseBodyBuilder":
        self._patch_employee_response_body.employee = employee
        return self
    
    def build(self) -> "PatchEmployeeResponseBody":
        return self._patch_employee_response_body