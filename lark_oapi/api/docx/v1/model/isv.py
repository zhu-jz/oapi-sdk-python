# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Isv(object):
    _types = {
        "component_id": str,
        "component_type_id": str,
    }

    def __init__(self, d=None):
        self.component_id: Optional[str] = None
        self.component_type_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "IsvBuilder":
        return IsvBuilder()


class IsvBuilder(object):
    def __init__(self) -> None:
        self._isv = Isv()

    def component_id(self, component_id: str) -> "IsvBuilder":
        self._isv.component_id = component_id
        return self

    def component_type_id(self, component_type_id: str) -> "IsvBuilder":
        self._isv.component_type_id = component_type_id
        return self

    def build(self) -> "Isv":
        return self._isv
