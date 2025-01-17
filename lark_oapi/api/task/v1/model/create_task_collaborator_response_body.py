# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .collaborator import Collaborator


class CreateTaskCollaboratorResponseBody(object):
    _types = {
        "collaborator": Collaborator,
    }

    def __init__(self, d=None):
        self.collaborator: Optional[Collaborator] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateTaskCollaboratorResponseBodyBuilder":
        return CreateTaskCollaboratorResponseBodyBuilder()


class CreateTaskCollaboratorResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_task_collaborator_response_body = CreateTaskCollaboratorResponseBody()

    def collaborator(self, collaborator: Collaborator) -> "CreateTaskCollaboratorResponseBodyBuilder":
        self._create_task_collaborator_response_body.collaborator = collaborator
        return self

    def build(self) -> "CreateTaskCollaboratorResponseBody":
        return self._create_task_collaborator_response_body
