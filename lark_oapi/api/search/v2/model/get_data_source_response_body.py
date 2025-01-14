# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .data_source import DataSource


class GetDataSourceResponseBody(object):
    _types = {
        "data_source": DataSource,
    }

    def __init__(self, d=None):
        self.data_source: Optional[DataSource] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetDataSourceResponseBodyBuilder":
        return GetDataSourceResponseBodyBuilder()


class GetDataSourceResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_data_source_response_body = GetDataSourceResponseBody()

    def data_source(self, data_source: DataSource) -> "GetDataSourceResponseBodyBuilder":
        self._get_data_source_response_body.data_source = data_source
        return self

    def build(self) -> "GetDataSourceResponseBody":
        return self._get_data_source_response_body
