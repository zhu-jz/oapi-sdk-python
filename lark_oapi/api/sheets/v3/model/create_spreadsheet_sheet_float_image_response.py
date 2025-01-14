# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_spreadsheet_sheet_float_image_response_body import CreateSpreadsheetSheetFloatImageResponseBody


class CreateSpreadsheetSheetFloatImageResponse(BaseResponse):
    _types = {
        "data": CreateSpreadsheetSheetFloatImageResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateSpreadsheetSheetFloatImageResponseBody] = None
        init(self, d, self._types)
