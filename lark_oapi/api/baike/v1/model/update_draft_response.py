# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .update_draft_response_body import UpdateDraftResponseBody


class UpdateDraftResponse(BaseResponse):
    _types = {
        "data": UpdateDraftResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[UpdateDraftResponseBody] = None
        init(self, d, self._types)
