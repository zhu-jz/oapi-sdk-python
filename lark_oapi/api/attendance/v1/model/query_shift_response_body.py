# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .flexible_rule import FlexibleRule
from .late_off_late_on_rule import LateOffLateOnRule
from .overtime_rule import OvertimeRule
from .punch_time_rule import PunchTimeRule
from .rest_rule import RestRule


class QueryShiftResponseBody(object):
    _types = {
        "shift_id": str,
        "shift_name": str,
        "punch_times": int,
        "sub_shift_leader_ids": List[str],
        "is_flexible": bool,
        "flexible_minutes": int,
        "flexible_rule": List[FlexibleRule],
        "no_need_off": bool,
        "punch_time_rule": List[PunchTimeRule],
        "late_off_late_on_rule": List[LateOffLateOnRule],
        "rest_time_rule": List[RestRule],
        "overtime_rule": List[OvertimeRule],
        "allow_punch_approval": bool,
    }

    def __init__(self, d=None):
        self.shift_id: Optional[str] = None
        self.shift_name: Optional[str] = None
        self.punch_times: Optional[int] = None
        self.sub_shift_leader_ids: Optional[List[str]] = None
        self.is_flexible: Optional[bool] = None
        self.flexible_minutes: Optional[int] = None
        self.flexible_rule: Optional[List[FlexibleRule]] = None
        self.no_need_off: Optional[bool] = None
        self.punch_time_rule: Optional[List[PunchTimeRule]] = None
        self.late_off_late_on_rule: Optional[List[LateOffLateOnRule]] = None
        self.rest_time_rule: Optional[List[RestRule]] = None
        self.overtime_rule: Optional[List[OvertimeRule]] = None
        self.allow_punch_approval: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QueryShiftResponseBodyBuilder":
        return QueryShiftResponseBodyBuilder()


class QueryShiftResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._query_shift_response_body = QueryShiftResponseBody()

    def shift_id(self, shift_id: str) -> "QueryShiftResponseBodyBuilder":
        self._query_shift_response_body.shift_id = shift_id
        return self

    def shift_name(self, shift_name: str) -> "QueryShiftResponseBodyBuilder":
        self._query_shift_response_body.shift_name = shift_name
        return self

    def punch_times(self, punch_times: int) -> "QueryShiftResponseBodyBuilder":
        self._query_shift_response_body.punch_times = punch_times
        return self

    def sub_shift_leader_ids(self, sub_shift_leader_ids: List[str]) -> "QueryShiftResponseBodyBuilder":
        self._query_shift_response_body.sub_shift_leader_ids = sub_shift_leader_ids
        return self

    def is_flexible(self, is_flexible: bool) -> "QueryShiftResponseBodyBuilder":
        self._query_shift_response_body.is_flexible = is_flexible
        return self

    def flexible_minutes(self, flexible_minutes: int) -> "QueryShiftResponseBodyBuilder":
        self._query_shift_response_body.flexible_minutes = flexible_minutes
        return self

    def flexible_rule(self, flexible_rule: List[FlexibleRule]) -> "QueryShiftResponseBodyBuilder":
        self._query_shift_response_body.flexible_rule = flexible_rule
        return self

    def no_need_off(self, no_need_off: bool) -> "QueryShiftResponseBodyBuilder":
        self._query_shift_response_body.no_need_off = no_need_off
        return self

    def punch_time_rule(self, punch_time_rule: List[PunchTimeRule]) -> "QueryShiftResponseBodyBuilder":
        self._query_shift_response_body.punch_time_rule = punch_time_rule
        return self

    def late_off_late_on_rule(self, late_off_late_on_rule: List[LateOffLateOnRule]) -> "QueryShiftResponseBodyBuilder":
        self._query_shift_response_body.late_off_late_on_rule = late_off_late_on_rule
        return self

    def rest_time_rule(self, rest_time_rule: List[RestRule]) -> "QueryShiftResponseBodyBuilder":
        self._query_shift_response_body.rest_time_rule = rest_time_rule
        return self

    def overtime_rule(self, overtime_rule: List[OvertimeRule]) -> "QueryShiftResponseBodyBuilder":
        self._query_shift_response_body.overtime_rule = overtime_rule
        return self

    def allow_punch_approval(self, allow_punch_approval: bool) -> "QueryShiftResponseBodyBuilder":
        self._query_shift_response_body.allow_punch_approval = allow_punch_approval
        return self

    def build(self) -> "QueryShiftResponseBody":
        return self._query_shift_response_body
