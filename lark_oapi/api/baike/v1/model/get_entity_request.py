# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetEntityRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.provider: Optional[str] = None
        self.outer_id: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.entity_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetEntityRequestBuilder":
        return GetEntityRequestBuilder()


class GetEntityRequestBuilder(object):

    def __init__(self) -> None:
        get_entity_request = GetEntityRequest()
        get_entity_request.http_method = HttpMethod.GET
        get_entity_request.uri = "/open-apis/baike/v1/entities/:entity_id"
        get_entity_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._get_entity_request: GetEntityRequest = get_entity_request

    def provider(self, provider: str) -> "GetEntityRequestBuilder":
        self._get_entity_request.provider = provider
        self._get_entity_request.add_query("provider", provider)
        return self

    def outer_id(self, outer_id: str) -> "GetEntityRequestBuilder":
        self._get_entity_request.outer_id = outer_id
        self._get_entity_request.add_query("outer_id", outer_id)
        return self

    def user_id_type(self, user_id_type: str) -> "GetEntityRequestBuilder":
        self._get_entity_request.user_id_type = user_id_type
        self._get_entity_request.add_query("user_id_type", user_id_type)
        return self

    def entity_id(self, entity_id: str) -> "GetEntityRequestBuilder":
        self._get_entity_request.entity_id = entity_id
        self._get_entity_request.paths["entity_id"] = str(entity_id)
        return self

    def build(self) -> GetEntityRequest:
        return self._get_entity_request
