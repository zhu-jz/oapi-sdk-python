# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .department import Department


class BatchDepartmentResponseBody(object):
    _types = {
        "items": List[Department],
    }

    def __init__(self, d=None):
        self.items: Optional[List[Department]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchDepartmentResponseBodyBuilder":
        return BatchDepartmentResponseBodyBuilder()


class BatchDepartmentResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_department_response_body = BatchDepartmentResponseBody()

    def items(self, items: List[Department]) -> "BatchDepartmentResponseBodyBuilder":
        self._batch_department_response_body.items = items
        return self

    def build(self) -> "BatchDepartmentResponseBody":
        return self._batch_department_response_body
