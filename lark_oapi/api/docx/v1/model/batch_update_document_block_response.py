# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .batch_update_document_block_response_body import BatchUpdateDocumentBlockResponseBody


class BatchUpdateDocumentBlockResponse(BaseResponse):
    _types = {
        "data": BatchUpdateDocumentBlockResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[BatchUpdateDocumentBlockResponseBody] = None
        init(self, d, self._types)
