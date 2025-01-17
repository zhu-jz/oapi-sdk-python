# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_pre_hire_response_body import ListPreHireResponseBody


class ListPreHireResponse(BaseResponse):
    _types = {
        "data": ListPreHireResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListPreHireResponseBody] = None
        init(self, d, self._types)
