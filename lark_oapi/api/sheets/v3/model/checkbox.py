# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Checkbox(object):
    _types = {
        "data_validation_id": int,
        "data_validiton_value": str,
    }

    def __init__(self, d=None):
        self.data_validation_id: Optional[int] = None
        self.data_validiton_value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CheckboxBuilder":
        return CheckboxBuilder()


class CheckboxBuilder(object):
    def __init__(self) -> None:
        self._checkbox = Checkbox()

    def data_validation_id(self, data_validation_id: int) -> "CheckboxBuilder":
        self._checkbox.data_validation_id = data_validation_id
        return self

    def data_validiton_value(self, data_validiton_value: str) -> "CheckboxBuilder":
        self._checkbox.data_validiton_value = data_validiton_value
        return self

    def build(self) -> "Checkbox":
        return self._checkbox
