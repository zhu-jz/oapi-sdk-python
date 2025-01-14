# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_group_response_body import CreateGroupResponseBody


class CreateGroupResponse(BaseResponse):
    _types = {
        "data": CreateGroupResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateGroupResponseBody] = None
        init(self, d, self._types)
