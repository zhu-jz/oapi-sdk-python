# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .common_schema import CommonSchema


class RegistrationSchema(object):
    _types = {
        "id": str,
        "name": str,
        "scenarios": List[int],
        "objects": List[CommonSchema],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.scenarios: Optional[List[int]] = None
        self.objects: Optional[List[CommonSchema]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RegistrationSchemaBuilder":
        return RegistrationSchemaBuilder()


class RegistrationSchemaBuilder(object):
    def __init__(self) -> None:
        self._registration_schema = RegistrationSchema()

    def id(self, id: str) -> "RegistrationSchemaBuilder":
        self._registration_schema.id = id
        return self

    def name(self, name: str) -> "RegistrationSchemaBuilder":
        self._registration_schema.name = name
        return self

    def scenarios(self, scenarios: List[int]) -> "RegistrationSchemaBuilder":
        self._registration_schema.scenarios = scenarios
        return self

    def objects(self, objects: List[CommonSchema]) -> "RegistrationSchemaBuilder":
        self._registration_schema.objects = objects
        return self

    def build(self) -> "RegistrationSchema":
        return self._registration_schema
