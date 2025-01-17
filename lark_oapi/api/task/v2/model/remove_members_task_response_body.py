# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .task import Task


class RemoveMembersTaskResponseBody(object):
    _types = {
        "task": Task,
    }

    def __init__(self, d=None):
        self.task: Optional[Task] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RemoveMembersTaskResponseBodyBuilder":
        return RemoveMembersTaskResponseBodyBuilder()


class RemoveMembersTaskResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._remove_members_task_response_body = RemoveMembersTaskResponseBody()

    def task(self, task: Task) -> "RemoveMembersTaskResponseBodyBuilder":
        self._remove_members_task_response_body.task = task
        return self

    def build(self) -> "RemoveMembersTaskResponseBody":
        return self._remove_members_task_response_body
