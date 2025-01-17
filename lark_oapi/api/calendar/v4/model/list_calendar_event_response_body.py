# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .calendar_event import CalendarEvent


class ListCalendarEventResponseBody(object):
    _types = {
        "has_more": bool,
        "page_token": str,
        "sync_token": str,
        "items": List[CalendarEvent],
    }

    def __init__(self, d=None):
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        self.sync_token: Optional[str] = None
        self.items: Optional[List[CalendarEvent]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListCalendarEventResponseBodyBuilder":
        return ListCalendarEventResponseBodyBuilder()


class ListCalendarEventResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_calendar_event_response_body = ListCalendarEventResponseBody()

    def has_more(self, has_more: bool) -> "ListCalendarEventResponseBodyBuilder":
        self._list_calendar_event_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListCalendarEventResponseBodyBuilder":
        self._list_calendar_event_response_body.page_token = page_token
        return self

    def sync_token(self, sync_token: str) -> "ListCalendarEventResponseBodyBuilder":
        self._list_calendar_event_response_body.sync_token = sync_token
        return self

    def items(self, items: List[CalendarEvent]) -> "ListCalendarEventResponseBodyBuilder":
        self._list_calendar_event_response_body.items = items
        return self

    def build(self) -> "ListCalendarEventResponseBody":
        return self._list_calendar_event_response_body
