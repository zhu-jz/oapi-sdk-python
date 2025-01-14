# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod
from lark_oapi.core.model import BaseRequest
from .resend_app_ticket_request_body import ResendAppTicketRequestBody


class ResendAppTicketRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[ResendAppTicketRequestBody] = None

    @staticmethod
    def builder() -> "ResendAppTicketRequestBuilder":
        return ResendAppTicketRequestBuilder()


class ResendAppTicketRequestBuilder(object):

    def __init__(self) -> None:
        resend_app_ticket_request = ResendAppTicketRequest()
        resend_app_ticket_request.http_method = HttpMethod.POST
        resend_app_ticket_request.uri = "/open-apis/auth/v3/app_ticket/resend"
        resend_app_ticket_request.token_types = {}
        self._resend_app_ticket_request: ResendAppTicketRequest = resend_app_ticket_request

    def request_body(self, request_body: ResendAppTicketRequestBody) -> "ResendAppTicketRequestBuilder":
        self._resend_app_ticket_request.request_body = request_body
        self._resend_app_ticket_request.body = request_body
        return self

    def build(self) -> ResendAppTicketRequest:
        return self._resend_app_ticket_request
