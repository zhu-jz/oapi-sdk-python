# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .message import Message


class GetMessageResponseBody(object):
    _types = {
        "items": List[Message],
    }

    def __init__(self, d=None):
        self.items: Optional[List[Message]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetMessageResponseBodyBuilder":
        return GetMessageResponseBodyBuilder()


class GetMessageResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_message_response_body = GetMessageResponseBody()

    def items(self, items: List[Message]) -> "GetMessageResponseBodyBuilder":
        self._get_message_response_body.items = items
        return self

    def build(self) -> "GetMessageResponseBody":
        return self._get_message_response_body
