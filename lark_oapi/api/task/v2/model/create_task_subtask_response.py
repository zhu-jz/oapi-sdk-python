# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_task_subtask_response_body import CreateTaskSubtaskResponseBody


class CreateTaskSubtaskResponse(BaseResponse):
    _types = {
        "data": CreateTaskSubtaskResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateTaskSubtaskResponseBody] = None
        init(self, d, self._types)
