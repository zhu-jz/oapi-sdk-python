# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class AlignmentStyle(object):
    _types = {
        "horizontal_alignment": str,
        "vertical_alignment": str,
    }

    def __init__(self, d):
        self.horizontal_alignment: Optional[str] = None
        self.vertical_alignment: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AlignmentStyleBuilder":
        return AlignmentStyleBuilder()


class AlignmentStyleBuilder(object):
    def __init__(self, alignment_style: AlignmentStyle = AlignmentStyle({})) -> None:
        self._alignment_style: AlignmentStyle = alignment_style
    
    def horizontal_alignment(self, horizontal_alignment: str) -> "AlignmentStyleBuilder":
        self._alignment_style.horizontal_alignment = horizontal_alignment
        return self
    
    def vertical_alignment(self, vertical_alignment: str) -> "AlignmentStyleBuilder":
        self._alignment_style.vertical_alignment = vertical_alignment
        return self
    
    def build(self) -> "AlignmentStyle":
        return self._alignment_style