# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class UserStatsDataFeature(object):
    _types = {
        "key": str,
        "value": str,
    }

    def __init__(self, d=None):
        self.key: Optional[str] = None
        self.value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserStatsDataFeatureBuilder":
        return UserStatsDataFeatureBuilder()


class UserStatsDataFeatureBuilder(object):
    def __init__(self) -> None:
        self._user_stats_data_feature = UserStatsDataFeature()

    def key(self, key: str) -> "UserStatsDataFeatureBuilder":
        self._user_stats_data_feature.key = key
        return self

    def value(self, value: str) -> "UserStatsDataFeatureBuilder":
        self._user_stats_data_feature.value = value
        return self

    def build(self) -> "UserStatsDataFeature":
        return self._user_stats_data_feature
