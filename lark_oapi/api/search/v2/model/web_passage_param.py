# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class WebPassageParam(object):
    _types = {
        "searchable": bool,
        "domains": List[str],
    }

    def __init__(self, d):
        self.searchable: Optional[bool] = None
        self.domains: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WebPassageParamBuilder":
        return WebPassageParamBuilder()


class WebPassageParamBuilder(object):
    def __init__(self, web_passage_param: WebPassageParam = WebPassageParam({})) -> None:
        self._web_passage_param: WebPassageParam = web_passage_param
    
    def searchable(self, searchable: bool) -> "WebPassageParamBuilder":
        self._web_passage_param.searchable = searchable
        return self
    
    def domains(self, domains: List[str]) -> "WebPassageParamBuilder":
        self._web_passage_param.domains = domains
        return self
    
    def build(self) -> "WebPassageParam":
        return self._web_passage_param