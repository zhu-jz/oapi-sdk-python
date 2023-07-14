# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .display_status import DisplayStatus


class Term(object):
    _types = {
        "key": str,
        "display_status": DisplayStatus,
    }

    def __init__(self, d):
        self.key: Optional[str] = None
        self.display_status: Optional[DisplayStatus] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TermBuilder":
        return TermBuilder()


class TermBuilder(object):
    def __init__(self, term: Term = Term({})) -> None:
        self._term: Term = term
    
    def key(self, key: str) -> "TermBuilder":
        self._term.key = key
        return self
    
    def display_status(self, display_status: DisplayStatus) -> "TermBuilder":
        self._term.display_status = display_status
        return self
    
    def build(self) -> "Term":
        return self._term