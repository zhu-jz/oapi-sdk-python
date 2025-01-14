# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Dimension(object):
    _types = {
        "major_dimension": str,
        "start_index": int,
        "end_index": int,
    }

    def __init__(self, d=None):
        self.major_dimension: Optional[str] = None
        self.start_index: Optional[int] = None
        self.end_index: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DimensionBuilder":
        return DimensionBuilder()


class DimensionBuilder(object):
    def __init__(self) -> None:
        self._dimension = Dimension()

    def major_dimension(self, major_dimension: str) -> "DimensionBuilder":
        self._dimension.major_dimension = major_dimension
        return self

    def start_index(self, start_index: int) -> "DimensionBuilder":
        self._dimension.start_index = start_index
        return self

    def end_index(self, end_index: int) -> "DimensionBuilder":
        self._dimension.end_index = end_index
        return self

    def build(self) -> "Dimension":
        return self._dimension
