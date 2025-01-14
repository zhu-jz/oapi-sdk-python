# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_country_region_response_body import GetCountryRegionResponseBody


class GetCountryRegionResponse(BaseResponse):
    _types = {
        "data": GetCountryRegionResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetCountryRegionResponseBody] = None
        init(self, d, self._types)
