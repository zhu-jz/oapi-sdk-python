# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_space_member_response_body import CreateSpaceMemberResponseBody


class CreateSpaceMemberResponse(BaseResponse):
    _types = {
        "data": CreateSpaceMemberResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreateSpaceMemberResponseBody] = None
        init(self, d, self._types)