# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .entity import Entity


class GetEntityResponseBody(object):
    _types = {
        "entity": Entity,
    }

    def __init__(self, d=None):
        self.entity: Optional[Entity] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetEntityResponseBodyBuilder":
        return GetEntityResponseBodyBuilder()


class GetEntityResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_entity_response_body = GetEntityResponseBody()

    def entity(self, entity: Entity) -> "GetEntityResponseBodyBuilder":
        self._get_entity_response_body.entity = entity
        return self

    def build(self) -> "GetEntityResponseBody":
        return self._get_entity_response_body
