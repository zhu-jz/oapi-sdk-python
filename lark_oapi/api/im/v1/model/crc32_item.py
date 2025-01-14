# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Crc32Item(object):
    _types = {
        "part_id": str,
        "crc32": str,
    }

    def __init__(self, d=None):
        self.part_id: Optional[str] = None
        self.crc32: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "Crc32ItemBuilder":
        return Crc32ItemBuilder()


class Crc32ItemBuilder(object):
    def __init__(self) -> None:
        self._crc32_item = Crc32Item()

    def part_id(self, part_id: str) -> "Crc32ItemBuilder":
        self._crc32_item.part_id = part_id
        return self

    def crc32(self, crc32: str) -> "Crc32ItemBuilder":
        self._crc32_item.crc32 = crc32
        return self

    def build(self) -> "Crc32Item":
        return self._crc32_item
