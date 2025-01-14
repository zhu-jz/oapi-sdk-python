# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class TransferOnboardApplicationRequestBody(object):
    _types = {
        "actual_onboard_time": int,
        "expected_conversion_time": int,
        "job_requirement_id": str,
        "operator_id": str,
        "onboard_city_code": str,
        "department": str,
        "leader": str,
        "sequence": str,
        "level": str,
        "employee_type": str,
    }

    def __init__(self, d=None):
        self.actual_onboard_time: Optional[int] = None
        self.expected_conversion_time: Optional[int] = None
        self.job_requirement_id: Optional[str] = None
        self.operator_id: Optional[str] = None
        self.onboard_city_code: Optional[str] = None
        self.department: Optional[str] = None
        self.leader: Optional[str] = None
        self.sequence: Optional[str] = None
        self.level: Optional[str] = None
        self.employee_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TransferOnboardApplicationRequestBodyBuilder":
        return TransferOnboardApplicationRequestBodyBuilder()


class TransferOnboardApplicationRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._transfer_onboard_application_request_body = TransferOnboardApplicationRequestBody()

    def actual_onboard_time(self, actual_onboard_time: int) -> "TransferOnboardApplicationRequestBodyBuilder":
        self._transfer_onboard_application_request_body.actual_onboard_time = actual_onboard_time
        return self

    def expected_conversion_time(self, expected_conversion_time: int) -> "TransferOnboardApplicationRequestBodyBuilder":
        self._transfer_onboard_application_request_body.expected_conversion_time = expected_conversion_time
        return self

    def job_requirement_id(self, job_requirement_id: str) -> "TransferOnboardApplicationRequestBodyBuilder":
        self._transfer_onboard_application_request_body.job_requirement_id = job_requirement_id
        return self

    def operator_id(self, operator_id: str) -> "TransferOnboardApplicationRequestBodyBuilder":
        self._transfer_onboard_application_request_body.operator_id = operator_id
        return self

    def onboard_city_code(self, onboard_city_code: str) -> "TransferOnboardApplicationRequestBodyBuilder":
        self._transfer_onboard_application_request_body.onboard_city_code = onboard_city_code
        return self

    def department(self, department: str) -> "TransferOnboardApplicationRequestBodyBuilder":
        self._transfer_onboard_application_request_body.department = department
        return self

    def leader(self, leader: str) -> "TransferOnboardApplicationRequestBodyBuilder":
        self._transfer_onboard_application_request_body.leader = leader
        return self

    def sequence(self, sequence: str) -> "TransferOnboardApplicationRequestBodyBuilder":
        self._transfer_onboard_application_request_body.sequence = sequence
        return self

    def level(self, level: str) -> "TransferOnboardApplicationRequestBodyBuilder":
        self._transfer_onboard_application_request_body.level = level
        return self

    def employee_type(self, employee_type: str) -> "TransferOnboardApplicationRequestBodyBuilder":
        self._transfer_onboard_application_request_body.employee_type = employee_type
        return self

    def build(self) -> "TransferOnboardApplicationRequestBody":
        return self._transfer_onboard_application_request_body
