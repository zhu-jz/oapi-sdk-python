# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .leave_request import LeaveRequest


class LeaveRequestHistoryLeaveResponseBody(object):
    _types = {
        "leave_request_list": List[LeaveRequest],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d=None):
        self.leave_request_list: Optional[List[LeaveRequest]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LeaveRequestHistoryLeaveResponseBodyBuilder":
        return LeaveRequestHistoryLeaveResponseBodyBuilder()


class LeaveRequestHistoryLeaveResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._leave_request_history_leave_response_body = LeaveRequestHistoryLeaveResponseBody()

    def leave_request_list(self,
                           leave_request_list: List[LeaveRequest]) -> "LeaveRequestHistoryLeaveResponseBodyBuilder":
        self._leave_request_history_leave_response_body.leave_request_list = leave_request_list
        return self

    def has_more(self, has_more: bool) -> "LeaveRequestHistoryLeaveResponseBodyBuilder":
        self._leave_request_history_leave_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "LeaveRequestHistoryLeaveResponseBodyBuilder":
        self._leave_request_history_leave_response_body.page_token = page_token
        return self

    def build(self) -> "LeaveRequestHistoryLeaveResponseBody":
        return self._leave_request_history_leave_response_body
