# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .app_recommend_rule_item_info import AppRecommendRuleItemInfo
from .app_recommend_rule_visibility_info import AppRecommendRuleVisibilityInfo


class AppRecommendRule(object):
    _types = {
        "id": str,
        "name": str,
        "status": str,
        "visibility_info": AppRecommendRuleVisibilityInfo,
        "recommend_item_infos": List[AppRecommendRuleItemInfo],
        "distributed_recommend_item_infos": List[AppRecommendRuleItemInfo],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.status: Optional[str] = None
        self.visibility_info: Optional[AppRecommendRuleVisibilityInfo] = None
        self.recommend_item_infos: Optional[List[AppRecommendRuleItemInfo]] = None
        self.distributed_recommend_item_infos: Optional[List[AppRecommendRuleItemInfo]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppRecommendRuleBuilder":
        return AppRecommendRuleBuilder()


class AppRecommendRuleBuilder(object):
    def __init__(self) -> None:
        self._app_recommend_rule = AppRecommendRule()

    def id(self, id: str) -> "AppRecommendRuleBuilder":
        self._app_recommend_rule.id = id
        return self

    def name(self, name: str) -> "AppRecommendRuleBuilder":
        self._app_recommend_rule.name = name
        return self

    def status(self, status: str) -> "AppRecommendRuleBuilder":
        self._app_recommend_rule.status = status
        return self

    def visibility_info(self, visibility_info: AppRecommendRuleVisibilityInfo) -> "AppRecommendRuleBuilder":
        self._app_recommend_rule.visibility_info = visibility_info
        return self

    def recommend_item_infos(self, recommend_item_infos: List[AppRecommendRuleItemInfo]) -> "AppRecommendRuleBuilder":
        self._app_recommend_rule.recommend_item_infos = recommend_item_infos
        return self

    def distributed_recommend_item_infos(self, distributed_recommend_item_infos: List[
        AppRecommendRuleItemInfo]) -> "AppRecommendRuleBuilder":
        self._app_recommend_rule.distributed_recommend_item_infos = distributed_recommend_item_infos
        return self

    def build(self) -> "AppRecommendRule":
        return self._app_recommend_rule
