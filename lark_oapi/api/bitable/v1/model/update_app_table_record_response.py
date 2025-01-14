# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .update_app_table_record_response_body import UpdateAppTableRecordResponseBody


class UpdateAppTableRecordResponse(BaseResponse):
    _types = {
        "data": UpdateAppTableRecordResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[UpdateAppTableRecordResponseBody] = None
        init(self, d, self._types)
