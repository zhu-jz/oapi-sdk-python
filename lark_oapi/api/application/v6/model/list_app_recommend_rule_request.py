# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListAppRecommendRuleRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.user_id_type: Optional[str] = None

    @staticmethod
    def builder() -> "ListAppRecommendRuleRequestBuilder":
        return ListAppRecommendRuleRequestBuilder()


class ListAppRecommendRuleRequestBuilder(object):

    def __init__(self) -> None:
        list_app_recommend_rule_request = ListAppRecommendRuleRequest()
        list_app_recommend_rule_request.http_method = HttpMethod.GET
        list_app_recommend_rule_request.uri = "/open-apis/application/v6/app_recommend_rules"
        list_app_recommend_rule_request.token_types = {AccessTokenType.TENANT}
        self._list_app_recommend_rule_request: ListAppRecommendRuleRequest = list_app_recommend_rule_request

    def page_size(self, page_size: int) -> "ListAppRecommendRuleRequestBuilder":
        self._list_app_recommend_rule_request.page_size = page_size
        self._list_app_recommend_rule_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListAppRecommendRuleRequestBuilder":
        self._list_app_recommend_rule_request.page_token = page_token
        self._list_app_recommend_rule_request.add_query("page_token", page_token)
        return self

    def user_id_type(self, user_id_type: str) -> "ListAppRecommendRuleRequestBuilder":
        self._list_app_recommend_rule_request.user_id_type = user_id_type
        self._list_app_recommend_rule_request.add_query("user_id_type", user_id_type)
        return self

    def build(self) -> ListAppRecommendRuleRequest:
        return self._list_app_recommend_rule_request
