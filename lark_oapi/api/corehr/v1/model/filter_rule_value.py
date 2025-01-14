# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class FilterRuleValue(object):
    _types = {
        "type": int,
        "value": str,
    }

    def __init__(self, d=None):
        self.type: Optional[int] = None
        self.value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FilterRuleValueBuilder":
        return FilterRuleValueBuilder()


class FilterRuleValueBuilder(object):
    def __init__(self) -> None:
        self._filter_rule_value = FilterRuleValue()

    def type(self, type: int) -> "FilterRuleValueBuilder":
        self._filter_rule_value.type = type
        return self

    def value(self, value: str) -> "FilterRuleValueBuilder":
        self._filter_rule_value.value = value
        return self

    def build(self) -> "FilterRuleValue":
        return self._filter_rule_value
