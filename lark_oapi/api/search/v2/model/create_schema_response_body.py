# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .schema import Schema


class CreateSchemaResponseBody(object):
    _types = {
        "schema": Schema,
    }

    def __init__(self, d=None):
        self.schema: Optional[Schema] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateSchemaResponseBodyBuilder":
        return CreateSchemaResponseBodyBuilder()


class CreateSchemaResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_schema_response_body = CreateSchemaResponseBody()

    def schema(self, schema: Schema) -> "CreateSchemaResponseBodyBuilder":
        self._create_schema_response_body.schema = schema
        return self

    def build(self) -> "CreateSchemaResponseBody":
        return self._create_schema_response_body
