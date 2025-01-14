# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .create_agent_skill_request_body import CreateAgentSkillRequestBody


class CreateAgentSkillRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[CreateAgentSkillRequestBody] = None

    @staticmethod
    def builder() -> "CreateAgentSkillRequestBuilder":
        return CreateAgentSkillRequestBuilder()


class CreateAgentSkillRequestBuilder(object):

    def __init__(self) -> None:
        create_agent_skill_request = CreateAgentSkillRequest()
        create_agent_skill_request.http_method = HttpMethod.POST
        create_agent_skill_request.uri = "/open-apis/helpdesk/v1/agent_skills"
        create_agent_skill_request.token_types = {AccessTokenType.USER}
        self._create_agent_skill_request: CreateAgentSkillRequest = create_agent_skill_request

    def request_body(self, request_body: CreateAgentSkillRequestBody) -> "CreateAgentSkillRequestBuilder":
        self._create_agent_skill_request.request_body = request_body
        self._create_agent_skill_request.body = request_body
        return self

    def build(self) -> CreateAgentSkillRequest:
        return self._create_agent_skill_request
