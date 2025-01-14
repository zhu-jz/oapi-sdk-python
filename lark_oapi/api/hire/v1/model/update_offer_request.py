# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .offer_info import OfferInfo


class UpdateOfferRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.offer_id: Optional[str] = None
        self.request_body: Optional[OfferInfo] = None

    @staticmethod
    def builder() -> "UpdateOfferRequestBuilder":
        return UpdateOfferRequestBuilder()


class UpdateOfferRequestBuilder(object):

    def __init__(self) -> None:
        update_offer_request = UpdateOfferRequest()
        update_offer_request.http_method = HttpMethod.PUT
        update_offer_request.uri = "/open-apis/hire/v1/offers/:offer_id"
        update_offer_request.token_types = {AccessTokenType.TENANT}
        self._update_offer_request: UpdateOfferRequest = update_offer_request

    def user_id_type(self, user_id_type: str) -> "UpdateOfferRequestBuilder":
        self._update_offer_request.user_id_type = user_id_type
        self._update_offer_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "UpdateOfferRequestBuilder":
        self._update_offer_request.department_id_type = department_id_type
        self._update_offer_request.add_query("department_id_type", department_id_type)
        return self

    def offer_id(self, offer_id: str) -> "UpdateOfferRequestBuilder":
        self._update_offer_request.offer_id = offer_id
        self._update_offer_request.paths["offer_id"] = str(offer_id)
        return self

    def request_body(self, request_body: OfferInfo) -> "UpdateOfferRequestBuilder":
        self._update_offer_request.request_body = request_body
        self._update_offer_request.body = request_body
        return self

    def build(self) -> UpdateOfferRequest:
        return self._update_offer_request
