# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CustomizedFieldDisplayItem(object):
    _types = {
        "id": str,
        "value": str,
        "key_name": str,
        "display_name": str,
        "position": int,
        "required": bool,
        "editable": bool,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.value: Optional[str] = None
        self.key_name: Optional[str] = None
        self.display_name: Optional[str] = None
        self.position: Optional[int] = None
        self.required: Optional[bool] = None
        self.editable: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CustomizedFieldDisplayItemBuilder":
        return CustomizedFieldDisplayItemBuilder()


class CustomizedFieldDisplayItemBuilder(object):
    def __init__(self) -> None:
        self._customized_field_display_item = CustomizedFieldDisplayItem()

    def id(self, id: str) -> "CustomizedFieldDisplayItemBuilder":
        self._customized_field_display_item.id = id
        return self

    def value(self, value: str) -> "CustomizedFieldDisplayItemBuilder":
        self._customized_field_display_item.value = value
        return self

    def key_name(self, key_name: str) -> "CustomizedFieldDisplayItemBuilder":
        self._customized_field_display_item.key_name = key_name
        return self

    def display_name(self, display_name: str) -> "CustomizedFieldDisplayItemBuilder":
        self._customized_field_display_item.display_name = display_name
        return self

    def position(self, position: int) -> "CustomizedFieldDisplayItemBuilder":
        self._customized_field_display_item.position = position
        return self

    def required(self, required: bool) -> "CustomizedFieldDisplayItemBuilder":
        self._customized_field_display_item.required = required
        return self

    def editable(self, editable: bool) -> "CustomizedFieldDisplayItemBuilder":
        self._customized_field_display_item.editable = editable
        return self

    def build(self) -> "CustomizedFieldDisplayItem":
        return self._customized_field_display_item
