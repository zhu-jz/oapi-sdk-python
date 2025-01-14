# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_file_subscription_response_body import GetFileSubscriptionResponseBody


class GetFileSubscriptionResponse(BaseResponse):
    _types = {
        "data": GetFileSubscriptionResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetFileSubscriptionResponseBody] = None
        init(self, d, self._types)
