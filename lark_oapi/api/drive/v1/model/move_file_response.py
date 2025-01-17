# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .move_file_response_body import MoveFileResponseBody


class MoveFileResponse(BaseResponse):
    _types = {
        "data": MoveFileResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[MoveFileResponseBody] = None
        init(self, d, self._types)
