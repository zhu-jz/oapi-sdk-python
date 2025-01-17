# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CreateUnitResponseBody(object):
    _types = {
        "unit_id": str,
    }

    def __init__(self, d=None):
        self.unit_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateUnitResponseBodyBuilder":
        return CreateUnitResponseBodyBuilder()


class CreateUnitResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_unit_response_body = CreateUnitResponseBody()

    def unit_id(self, unit_id: str) -> "CreateUnitResponseBodyBuilder":
        self._create_unit_response_body.unit_id = unit_id
        return self

    def build(self) -> "CreateUnitResponseBody":
        return self._create_unit_response_body
