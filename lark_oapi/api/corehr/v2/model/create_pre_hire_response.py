# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_pre_hire_response_body import CreatePreHireResponseBody


class CreatePreHireResponse(BaseResponse):
    _types = {
        "data": CreatePreHireResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreatePreHireResponseBody] = None
        init(self, d, self._types)
