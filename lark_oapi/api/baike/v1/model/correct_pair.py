# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CorrectPair(object):
    _types = {
        "source_text": str,
        "target_text": str,
        "total": int,
    }

    def __init__(self, d=None):
        self.source_text: Optional[str] = None
        self.target_text: Optional[str] = None
        self.total: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CorrectPairBuilder":
        return CorrectPairBuilder()


class CorrectPairBuilder(object):
    def __init__(self) -> None:
        self._correct_pair = CorrectPair()

    def source_text(self, source_text: str) -> "CorrectPairBuilder":
        self._correct_pair.source_text = source_text
        return self

    def target_text(self, target_text: str) -> "CorrectPairBuilder":
        self._correct_pair.target_text = target_text
        return self

    def total(self, total: int) -> "CorrectPairBuilder":
        self._correct_pair.total = total
        return self

    def build(self) -> "CorrectPair":
        return self._correct_pair
