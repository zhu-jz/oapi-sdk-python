# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .reminder import Reminder


class CreateTaskReminderRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.task_id: Optional[str] = None
        self.request_body: Optional[Reminder] = None

    @staticmethod
    def builder() -> "CreateTaskReminderRequestBuilder":
        return CreateTaskReminderRequestBuilder()


class CreateTaskReminderRequestBuilder(object):

    def __init__(self) -> None:
        create_task_reminder_request = CreateTaskReminderRequest()
        create_task_reminder_request.http_method = HttpMethod.POST
        create_task_reminder_request.uri = "/open-apis/task/v1/tasks/:task_id/reminders"
        create_task_reminder_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._create_task_reminder_request: CreateTaskReminderRequest = create_task_reminder_request

    def task_id(self, task_id: str) -> "CreateTaskReminderRequestBuilder":
        self._create_task_reminder_request.task_id = task_id
        self._create_task_reminder_request.paths["task_id"] = str(task_id)
        return self

    def request_body(self, request_body: Reminder) -> "CreateTaskReminderRequestBuilder":
        self._create_task_reminder_request.request_body = request_body
        self._create_task_reminder_request.body = request_body
        return self

    def build(self) -> CreateTaskReminderRequest:
        return self._create_task_reminder_request
