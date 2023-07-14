# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .find_spreadsheet_sheet_response_body import FindSpreadsheetSheetResponseBody


class FindSpreadsheetSheetResponse(BaseResponse):
    _types = {
        "data": FindSpreadsheetSheetResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[FindSpreadsheetSheetResponseBody] = None
        init(self, d, self._types)