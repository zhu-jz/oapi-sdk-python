# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class QueryUserStatsFieldRequestBody(object):
    _types = {
        "locale": str,
        "stats_type": str,
        "start_date": int,
        "end_date": int,
    }

    def __init__(self, d=None):
        self.locale: Optional[str] = None
        self.stats_type: Optional[str] = None
        self.start_date: Optional[int] = None
        self.end_date: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QueryUserStatsFieldRequestBodyBuilder":
        return QueryUserStatsFieldRequestBodyBuilder()


class QueryUserStatsFieldRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._query_user_stats_field_request_body = QueryUserStatsFieldRequestBody()

    def locale(self, locale: str) -> "QueryUserStatsFieldRequestBodyBuilder":
        self._query_user_stats_field_request_body.locale = locale
        return self

    def stats_type(self, stats_type: str) -> "QueryUserStatsFieldRequestBodyBuilder":
        self._query_user_stats_field_request_body.stats_type = stats_type
        return self

    def start_date(self, start_date: int) -> "QueryUserStatsFieldRequestBodyBuilder":
        self._query_user_stats_field_request_body.start_date = start_date
        return self

    def end_date(self, end_date: int) -> "QueryUserStatsFieldRequestBodyBuilder":
        self._query_user_stats_field_request_body.end_date = end_date
        return self

    def build(self) -> "QueryUserStatsFieldRequestBody":
        return self._query_user_stats_field_request_body
