# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_application_response_body import CreateApplicationResponseBody


class CreateApplicationResponse(BaseResponse):
    _types = {
        "data": CreateApplicationResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateApplicationResponseBody] = None
        init(self, d, self._types)
