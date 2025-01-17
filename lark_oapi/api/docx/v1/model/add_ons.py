# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class AddOns(object):
    _types = {
        "component_id": str,
        "component_type_id": str,
        "record": str,
    }

    def __init__(self, d=None):
        self.component_id: Optional[str] = None
        self.component_type_id: Optional[str] = None
        self.record: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AddOnsBuilder":
        return AddOnsBuilder()


class AddOnsBuilder(object):
    def __init__(self) -> None:
        self._add_ons = AddOns()

    def component_id(self, component_id: str) -> "AddOnsBuilder":
        self._add_ons.component_id = component_id
        return self

    def component_type_id(self, component_type_id: str) -> "AddOnsBuilder":
        self._add_ons.component_type_id = component_type_id
        return self

    def record(self, record: str) -> "AddOnsBuilder":
        self._add_ons.record = record
        return self

    def build(self) -> "AddOns":
        return self._add_ons
