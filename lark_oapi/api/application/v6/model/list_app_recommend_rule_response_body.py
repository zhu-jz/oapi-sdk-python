# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .app_recommend_rule import AppRecommendRule


class ListAppRecommendRuleResponseBody(object):
    _types = {
        "rules": List[AppRecommendRule],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.rules: Optional[List[AppRecommendRule]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListAppRecommendRuleResponseBodyBuilder":
        return ListAppRecommendRuleResponseBodyBuilder()


class ListAppRecommendRuleResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_app_recommend_rule_response_body = ListAppRecommendRuleResponseBody()

    def rules(self, rules: List[AppRecommendRule]) -> "ListAppRecommendRuleResponseBodyBuilder":
        self._list_app_recommend_rule_response_body.rules = rules
        return self

    def page_token(self, page_token: str) -> "ListAppRecommendRuleResponseBodyBuilder":
        self._list_app_recommend_rule_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListAppRecommendRuleResponseBodyBuilder":
        self._list_app_recommend_rule_response_body.has_more = has_more
        return self

    def build(self) -> "ListAppRecommendRuleResponseBody":
        return self._list_app_recommend_rule_response_body
