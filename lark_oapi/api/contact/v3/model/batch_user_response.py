# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .batch_user_response_body import BatchUserResponseBody


class BatchUserResponse(BaseResponse):
    _types = {
        "data": BatchUserResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[BatchUserResponseBody] = None
        init(self, d, self._types)