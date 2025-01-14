# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class RegistrationSchemaInfo(object):
    _types = {
        "schema_id": str,
        "name": str,
    }

    def __init__(self, d=None):
        self.schema_id: Optional[str] = None
        self.name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RegistrationSchemaInfoBuilder":
        return RegistrationSchemaInfoBuilder()


class RegistrationSchemaInfoBuilder(object):
    def __init__(self) -> None:
        self._registration_schema_info = RegistrationSchemaInfo()

    def schema_id(self, schema_id: str) -> "RegistrationSchemaInfoBuilder":
        self._registration_schema_info.schema_id = schema_id
        return self

    def name(self, name: str) -> "RegistrationSchemaInfoBuilder":
        self._registration_schema_info.name = name
        return self

    def build(self) -> "RegistrationSchemaInfo":
        return self._registration_schema_info
