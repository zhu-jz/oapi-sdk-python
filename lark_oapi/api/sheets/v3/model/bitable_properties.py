# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class BitableProperties(object):
    _types = {
        "bitable_token": str,
        "table_id": str,
    }

    def __init__(self, d=None):
        self.bitable_token: Optional[str] = None
        self.table_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BitablePropertiesBuilder":
        return BitablePropertiesBuilder()


class BitablePropertiesBuilder(object):
    def __init__(self) -> None:
        self._bitable_properties = BitableProperties()

    def bitable_token(self, bitable_token: str) -> "BitablePropertiesBuilder":
        self._bitable_properties.bitable_token = bitable_token
        return self

    def table_id(self, table_id: str) -> "BitablePropertiesBuilder":
        self._bitable_properties.table_id = table_id
        return self

    def build(self) -> "BitableProperties":
        return self._bitable_properties
