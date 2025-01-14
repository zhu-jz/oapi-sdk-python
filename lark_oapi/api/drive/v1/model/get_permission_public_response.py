# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_permission_public_response_body import GetPermissionPublicResponseBody


class GetPermissionPublicResponse(BaseResponse):
    _types = {
        "data": GetPermissionPublicResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetPermissionPublicResponseBody] = None
        init(self, d, self._types)
