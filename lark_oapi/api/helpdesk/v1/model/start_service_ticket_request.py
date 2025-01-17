# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .start_service_ticket_request_body import StartServiceTicketRequestBody


class StartServiceTicketRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[StartServiceTicketRequestBody] = None

    @staticmethod
    def builder() -> "StartServiceTicketRequestBuilder":
        return StartServiceTicketRequestBuilder()


class StartServiceTicketRequestBuilder(object):

    def __init__(self) -> None:
        start_service_ticket_request = StartServiceTicketRequest()
        start_service_ticket_request.http_method = HttpMethod.POST
        start_service_ticket_request.uri = "/open-apis/helpdesk/v1/start_service"
        start_service_ticket_request.token_types = {AccessTokenType.TENANT}
        self._start_service_ticket_request: StartServiceTicketRequest = start_service_ticket_request

    def request_body(self, request_body: StartServiceTicketRequestBody) -> "StartServiceTicketRequestBuilder":
        self._start_service_ticket_request.request_body = request_body
        self._start_service_ticket_request.body = request_body
        return self

    def build(self) -> StartServiceTicketRequest:
        return self._start_service_ticket_request
