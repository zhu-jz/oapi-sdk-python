# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .external_instance import ExternalInstance


class CreateExternalInstanceResponseBody(object):
    _types = {
        "data": ExternalInstance,
    }

    def __init__(self, d=None):
        self.data: Optional[ExternalInstance] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateExternalInstanceResponseBodyBuilder":
        return CreateExternalInstanceResponseBodyBuilder()


class CreateExternalInstanceResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_external_instance_response_body = CreateExternalInstanceResponseBody()

    def data(self, data: ExternalInstance) -> "CreateExternalInstanceResponseBodyBuilder":
        self._create_external_instance_response_body.data = data
        return self

    def build(self) -> "CreateExternalInstanceResponseBody":
        return self._create_external_instance_response_body
