# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_contract_response_body import GetContractResponseBody


class GetContractResponse(BaseResponse):
    _types = {
        "data": GetContractResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetContractResponseBody] = None
        init(self, d, self._types)
