# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_badge_grant_response_body import ListBadgeGrantResponseBody


class ListBadgeGrantResponse(BaseResponse):
    _types = {
        "data": ListBadgeGrantResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListBadgeGrantResponseBody] = None
        init(self, d, self._types)
