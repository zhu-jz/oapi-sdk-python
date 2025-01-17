# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .patch_agent_schedules_request_body import PatchAgentSchedulesRequestBody


class PatchAgentSchedulesRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.agent_id: Optional[str] = None
        self.request_body: Optional[PatchAgentSchedulesRequestBody] = None

    @staticmethod
    def builder() -> "PatchAgentSchedulesRequestBuilder":
        return PatchAgentSchedulesRequestBuilder()


class PatchAgentSchedulesRequestBuilder(object):

    def __init__(self) -> None:
        patch_agent_schedules_request = PatchAgentSchedulesRequest()
        patch_agent_schedules_request.http_method = HttpMethod.PATCH
        patch_agent_schedules_request.uri = "/open-apis/helpdesk/v1/agents/:agent_id/schedules"
        patch_agent_schedules_request.token_types = {AccessTokenType.USER}
        self._patch_agent_schedules_request: PatchAgentSchedulesRequest = patch_agent_schedules_request

    def agent_id(self, agent_id: str) -> "PatchAgentSchedulesRequestBuilder":
        self._patch_agent_schedules_request.agent_id = agent_id
        self._patch_agent_schedules_request.paths["agent_id"] = str(agent_id)
        return self

    def request_body(self, request_body: PatchAgentSchedulesRequestBody) -> "PatchAgentSchedulesRequestBuilder":
        self._patch_agent_schedules_request.request_body = request_body
        self._patch_agent_schedules_request.body = request_body
        return self

    def build(self) -> PatchAgentSchedulesRequest:
        return self._patch_agent_schedules_request
