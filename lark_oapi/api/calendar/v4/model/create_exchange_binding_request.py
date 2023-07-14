# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .exchange_binding import ExchangeBinding


class CreateExchangeBindingRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[ExchangeBinding] = None

    @staticmethod
    def builder() -> "CreateExchangeBindingRequestBuilder":
        return CreateExchangeBindingRequestBuilder()


class CreateExchangeBindingRequestBuilder(object):

    def __init__(self, create_exchange_binding_request: CreateExchangeBindingRequest = CreateExchangeBindingRequest()) -> None:
        create_exchange_binding_request.http_method = HttpMethod.POST
        create_exchange_binding_request.uri = "/open-apis/calendar/v4/exchange_bindings"
        create_exchange_binding_request.token_types = {AccessTokenType.USER}
        self._create_exchange_binding_request: CreateExchangeBindingRequest = create_exchange_binding_request
    
    def user_id_type(self, user_id_type: str) -> "CreateExchangeBindingRequestBuilder":
        self._create_exchange_binding_request.user_id_type = user_id_type
        self._create_exchange_binding_request.queries["user_id_type"] = str(user_id_type)
        return self
    
    def request_body(self, request_body: ExchangeBinding) -> "CreateExchangeBindingRequestBuilder":
        self._create_exchange_binding_request.request_body = request_body
        self._create_exchange_binding_request.body = request_body
        return self

    def build(self) -> CreateExchangeBindingRequest:
        return self._create_exchange_binding_request