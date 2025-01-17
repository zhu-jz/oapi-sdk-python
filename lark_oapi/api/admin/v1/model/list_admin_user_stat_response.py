# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_admin_user_stat_response_body import ListAdminUserStatResponseBody


class ListAdminUserStatResponse(BaseResponse):
    _types = {
        "data": ListAdminUserStatResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListAdminUserStatResponseBody] = None
        init(self, d, self._types)
