# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Job(object):
    _types = {
        "id": int,
        "name": str,
    }

    def __init__(self, d=None):
        self.id: Optional[int] = None
        self.name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobBuilder":
        return JobBuilder()


class JobBuilder(object):
    def __init__(self) -> None:
        self._job = Job()

    def id(self, id: int) -> "JobBuilder":
        self._job.id = id
        return self

    def name(self, name: str) -> "JobBuilder":
        self._job.name = name
        return self

    def build(self) -> "Job":
        return self._job
