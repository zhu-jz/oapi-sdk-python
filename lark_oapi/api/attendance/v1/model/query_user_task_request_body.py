# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class QueryUserTaskRequestBody(object):
    _types = {
        "user_ids": List[str],
        "check_date_from": int,
        "check_date_to": int,
        "need_overtime_result": bool,
    }

    def __init__(self, d=None):
        self.user_ids: Optional[List[str]] = None
        self.check_date_from: Optional[int] = None
        self.check_date_to: Optional[int] = None
        self.need_overtime_result: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QueryUserTaskRequestBodyBuilder":
        return QueryUserTaskRequestBodyBuilder()


class QueryUserTaskRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._query_user_task_request_body = QueryUserTaskRequestBody()

    def user_ids(self, user_ids: List[str]) -> "QueryUserTaskRequestBodyBuilder":
        self._query_user_task_request_body.user_ids = user_ids
        return self

    def check_date_from(self, check_date_from: int) -> "QueryUserTaskRequestBodyBuilder":
        self._query_user_task_request_body.check_date_from = check_date_from
        return self

    def check_date_to(self, check_date_to: int) -> "QueryUserTaskRequestBodyBuilder":
        self._query_user_task_request_body.check_date_to = check_date_to
        return self

    def need_overtime_result(self, need_overtime_result: bool) -> "QueryUserTaskRequestBodyBuilder":
        self._query_user_task_request_body.need_overtime_result = need_overtime_result
        return self

    def build(self) -> "QueryUserTaskRequestBody":
        return self._query_user_task_request_body
