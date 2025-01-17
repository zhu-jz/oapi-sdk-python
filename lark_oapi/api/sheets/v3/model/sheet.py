# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .grid_properties import GridProperties
from .merge_range import MergeRange


class Sheet(object):
    _types = {
        "sheet_id": str,
        "title": str,
        "index": int,
        "hidden": bool,
        "grid_properties": GridProperties,
        "resource_type": str,
        "merges": List[MergeRange],
    }

    def __init__(self, d=None):
        self.sheet_id: Optional[str] = None
        self.title: Optional[str] = None
        self.index: Optional[int] = None
        self.hidden: Optional[bool] = None
        self.grid_properties: Optional[GridProperties] = None
        self.resource_type: Optional[str] = None
        self.merges: Optional[List[MergeRange]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SheetBuilder":
        return SheetBuilder()


class SheetBuilder(object):
    def __init__(self) -> None:
        self._sheet = Sheet()

    def sheet_id(self, sheet_id: str) -> "SheetBuilder":
        self._sheet.sheet_id = sheet_id
        return self

    def title(self, title: str) -> "SheetBuilder":
        self._sheet.title = title
        return self

    def index(self, index: int) -> "SheetBuilder":
        self._sheet.index = index
        return self

    def hidden(self, hidden: bool) -> "SheetBuilder":
        self._sheet.hidden = hidden
        return self

    def grid_properties(self, grid_properties: GridProperties) -> "SheetBuilder":
        self._sheet.grid_properties = grid_properties
        return self

    def resource_type(self, resource_type: str) -> "SheetBuilder":
        self._sheet.resource_type = resource_type
        return self

    def merges(self, merges: List[MergeRange]) -> "SheetBuilder":
        self._sheet.merges = merges
        return self

    def build(self) -> "Sheet":
        return self._sheet
