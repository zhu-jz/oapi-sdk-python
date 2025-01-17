# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .entity import Entity


class ListEntityResponseBody(object):
    _types = {
        "entities": List[Entity],
        "page_token": str,
    }

    def __init__(self, d=None):
        self.entities: Optional[List[Entity]] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListEntityResponseBodyBuilder":
        return ListEntityResponseBodyBuilder()


class ListEntityResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_entity_response_body = ListEntityResponseBody()

    def entities(self, entities: List[Entity]) -> "ListEntityResponseBodyBuilder":
        self._list_entity_response_body.entities = entities
        return self

    def page_token(self, page_token: str) -> "ListEntityResponseBodyBuilder":
        self._list_entity_response_body.page_token = page_token
        return self

    def build(self) -> "ListEntityResponseBody":
        return self._list_entity_response_body
