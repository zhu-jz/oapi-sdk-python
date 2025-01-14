# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .user_task import UserTask


class QueryUserTaskResponseBody(object):
    _types = {
        "user_task_results": List[UserTask],
        "invalid_user_ids": List[str],
        "unauthorized_user_ids": List[str],
    }

    def __init__(self, d=None):
        self.user_task_results: Optional[List[UserTask]] = None
        self.invalid_user_ids: Optional[List[str]] = None
        self.unauthorized_user_ids: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QueryUserTaskResponseBodyBuilder":
        return QueryUserTaskResponseBodyBuilder()


class QueryUserTaskResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._query_user_task_response_body = QueryUserTaskResponseBody()

    def user_task_results(self, user_task_results: List[UserTask]) -> "QueryUserTaskResponseBodyBuilder":
        self._query_user_task_response_body.user_task_results = user_task_results
        return self

    def invalid_user_ids(self, invalid_user_ids: List[str]) -> "QueryUserTaskResponseBodyBuilder":
        self._query_user_task_response_body.invalid_user_ids = invalid_user_ids
        return self

    def unauthorized_user_ids(self, unauthorized_user_ids: List[str]) -> "QueryUserTaskResponseBodyBuilder":
        self._query_user_task_response_body.unauthorized_user_ids = unauthorized_user_ids
        return self

    def build(self) -> "QueryUserTaskResponseBody":
        return self._query_user_task_response_body
