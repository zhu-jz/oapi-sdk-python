# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteUnitRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.unit_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteUnitRequestBuilder":
        return DeleteUnitRequestBuilder()


class DeleteUnitRequestBuilder(object):

    def __init__(self) -> None:
        delete_unit_request = DeleteUnitRequest()
        delete_unit_request.http_method = HttpMethod.DELETE
        delete_unit_request.uri = "/open-apis/contact/v3/unit/:unit_id"
        delete_unit_request.token_types = {AccessTokenType.TENANT}
        self._delete_unit_request: DeleteUnitRequest = delete_unit_request

    def unit_id(self, unit_id: str) -> "DeleteUnitRequestBuilder":
        self._delete_unit_request.unit_id = unit_id
        self._delete_unit_request.paths["unit_id"] = str(unit_id)
        return self

    def build(self) -> DeleteUnitRequest:
        return self._delete_unit_request
