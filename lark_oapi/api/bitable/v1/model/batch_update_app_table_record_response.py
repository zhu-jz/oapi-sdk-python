# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .batch_update_app_table_record_response_body import BatchUpdateAppTableRecordResponseBody


class BatchUpdateAppTableRecordResponse(BaseResponse):
    _types = {
        "data": BatchUpdateAppTableRecordResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[BatchUpdateAppTableRecordResponseBody] = None
        init(self, d, self._types)
