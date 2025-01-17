# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .collaborator import Collaborator


class CreateTaskCollaboratorRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.task_id: Optional[str] = None
        self.request_body: Optional[Collaborator] = None

    @staticmethod
    def builder() -> "CreateTaskCollaboratorRequestBuilder":
        return CreateTaskCollaboratorRequestBuilder()


class CreateTaskCollaboratorRequestBuilder(object):

    def __init__(self) -> None:
        create_task_collaborator_request = CreateTaskCollaboratorRequest()
        create_task_collaborator_request.http_method = HttpMethod.POST
        create_task_collaborator_request.uri = "/open-apis/task/v1/tasks/:task_id/collaborators"
        create_task_collaborator_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._create_task_collaborator_request: CreateTaskCollaboratorRequest = create_task_collaborator_request

    def user_id_type(self, user_id_type: str) -> "CreateTaskCollaboratorRequestBuilder":
        self._create_task_collaborator_request.user_id_type = user_id_type
        self._create_task_collaborator_request.add_query("user_id_type", user_id_type)
        return self

    def task_id(self, task_id: str) -> "CreateTaskCollaboratorRequestBuilder":
        self._create_task_collaborator_request.task_id = task_id
        self._create_task_collaborator_request.paths["task_id"] = str(task_id)
        return self

    def request_body(self, request_body: Collaborator) -> "CreateTaskCollaboratorRequestBuilder":
        self._create_task_collaborator_request.request_body = request_body
        self._create_task_collaborator_request.body = request_body
        return self

    def build(self) -> CreateTaskCollaboratorRequest:
        return self._create_task_collaborator_request
