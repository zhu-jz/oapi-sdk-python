# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class TaskCheckFileResponseBody(object):
    _types = {
        "status": str,
    }

    def __init__(self, d=None):
        self.status: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TaskCheckFileResponseBodyBuilder":
        return TaskCheckFileResponseBodyBuilder()


class TaskCheckFileResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._task_check_file_response_body = TaskCheckFileResponseBody()

    def status(self, status: str) -> "TaskCheckFileResponseBodyBuilder":
        self._task_check_file_response_body.status = status
        return self

    def build(self) -> "TaskCheckFileResponseBody":
        return self._task_check_file_response_body
