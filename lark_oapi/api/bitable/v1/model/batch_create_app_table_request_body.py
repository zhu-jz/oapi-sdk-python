# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .req_table import ReqTable


class BatchCreateAppTableRequestBody(object):
    _types = {
        "tables": List[ReqTable],
    }

    def __init__(self, d=None):
        self.tables: Optional[List[ReqTable]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchCreateAppTableRequestBodyBuilder":
        return BatchCreateAppTableRequestBodyBuilder()


class BatchCreateAppTableRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_create_app_table_request_body = BatchCreateAppTableRequestBody()

    def tables(self, tables: List[ReqTable]) -> "BatchCreateAppTableRequestBodyBuilder":
        self._batch_create_app_table_request_body.tables = tables
        return self

    def build(self) -> "BatchCreateAppTableRequestBody":
        return self._batch_create_app_table_request_body
