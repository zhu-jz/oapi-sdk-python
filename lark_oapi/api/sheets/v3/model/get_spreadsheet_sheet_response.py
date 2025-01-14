# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_spreadsheet_sheet_response_body import GetSpreadsheetSheetResponseBody


class GetSpreadsheetSheetResponse(BaseResponse):
    _types = {
        "data": GetSpreadsheetSheetResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetSpreadsheetSheetResponseBody] = None
        init(self, d, self._types)
