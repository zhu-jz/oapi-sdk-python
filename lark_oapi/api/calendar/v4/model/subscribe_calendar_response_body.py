# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .calendar import Calendar


class SubscribeCalendarResponseBody(object):
    _types = {
        "calendar": Calendar,
    }

    def __init__(self, d):
        self.calendar: Optional[Calendar] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SubscribeCalendarResponseBodyBuilder":
        return SubscribeCalendarResponseBodyBuilder()


class SubscribeCalendarResponseBodyBuilder(object):
    def __init__(self, subscribe_calendar_response_body: SubscribeCalendarResponseBody = SubscribeCalendarResponseBody({})) -> None:
        self._subscribe_calendar_response_body: SubscribeCalendarResponseBody = subscribe_calendar_response_body
    
    def calendar(self, calendar: Calendar) -> "SubscribeCalendarResponseBodyBuilder":
        self._subscribe_calendar_response_body.calendar = calendar
        return self
    
    def build(self) -> "SubscribeCalendarResponseBody":
        return self._subscribe_calendar_response_body