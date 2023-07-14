# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class EcoExamCreateEventMobile(object):
    _types = {
        "code": str,
        "number": str,
    }

    def __init__(self, d):
        self.code: Optional[str] = None
        self.number: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EcoExamCreateEventMobileBuilder":
        return EcoExamCreateEventMobileBuilder()


class EcoExamCreateEventMobileBuilder(object):
    def __init__(self, eco_exam_create_event_mobile: EcoExamCreateEventMobile = EcoExamCreateEventMobile({})) -> None:
        self._eco_exam_create_event_mobile: EcoExamCreateEventMobile = eco_exam_create_event_mobile
    
    def code(self, code: str) -> "EcoExamCreateEventMobileBuilder":
        self._eco_exam_create_event_mobile.code = code
        return self
    
    def number(self, number: str) -> "EcoExamCreateEventMobileBuilder":
        self._eco_exam_create_event_mobile.number = number
        return self
    
    def build(self) -> "EcoExamCreateEventMobile":
        return self._eco_exam_create_event_mobile