# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .float_image import FloatImage


class PatchSpreadsheetSheetFloatImageResponseBody(object):
    _types = {
        "float_image": FloatImage,
    }

    def __init__(self, d=None):
        self.float_image: Optional[FloatImage] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchSpreadsheetSheetFloatImageResponseBodyBuilder":
        return PatchSpreadsheetSheetFloatImageResponseBodyBuilder()


class PatchSpreadsheetSheetFloatImageResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_spreadsheet_sheet_float_image_response_body = PatchSpreadsheetSheetFloatImageResponseBody()

    def float_image(self, float_image: FloatImage) -> "PatchSpreadsheetSheetFloatImageResponseBodyBuilder":
        self._patch_spreadsheet_sheet_float_image_response_body.float_image = float_image
        return self

    def build(self) -> "PatchSpreadsheetSheetFloatImageResponseBody":
        return self._patch_spreadsheet_sheet_float_image_response_body
