# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_company_response_body import CreateCompanyResponseBody


class CreateCompanyResponse(BaseResponse):
    _types = {
        "data": CreateCompanyResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[CreateCompanyResponseBody] = None
        init(self, d, self._types)