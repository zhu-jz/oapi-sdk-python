# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_scope_response_body import ListScopeResponseBody


class ListScopeResponse(BaseResponse):
    _types = {
        "data": ListScopeResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ListScopeResponseBody] = None
        init(self, d, self._types)