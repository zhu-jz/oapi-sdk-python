# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_subregion_response_body import GetSubregionResponseBody


class GetSubregionResponse(BaseResponse):
    _types = {
        "data": GetSubregionResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetSubregionResponseBody] = None
        init(self, d, self._types)
