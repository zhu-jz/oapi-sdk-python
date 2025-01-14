# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class WorkLocation(object):
    _types = {
        "id": int,
        "name": str,
    }

    def __init__(self, d=None):
        self.id: Optional[int] = None
        self.name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WorkLocationBuilder":
        return WorkLocationBuilder()


class WorkLocationBuilder(object):
    def __init__(self) -> None:
        self._work_location = WorkLocation()

    def id(self, id: int) -> "WorkLocationBuilder":
        self._work_location.id = id
        return self

    def name(self, name: str) -> "WorkLocationBuilder":
        self._work_location.name = name
        return self

    def build(self) -> "WorkLocation":
        return self._work_location
