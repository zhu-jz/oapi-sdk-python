# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .leave_request_history_leave_response_body import LeaveRequestHistoryLeaveResponseBody


class LeaveRequestHistoryLeaveResponse(BaseResponse):
    _types = {
        "data": LeaveRequestHistoryLeaveResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[LeaveRequestHistoryLeaveResponseBody] = None
        init(self, d, self._types)
