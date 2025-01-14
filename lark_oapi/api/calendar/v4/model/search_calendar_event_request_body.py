# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .event_search_filter import EventSearchFilter


class SearchCalendarEventRequestBody(object):
    _types = {
        "query": str,
        "filter": EventSearchFilter,
    }

    def __init__(self, d=None):
        self.query: Optional[str] = None
        self.filter: Optional[EventSearchFilter] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchCalendarEventRequestBodyBuilder":
        return SearchCalendarEventRequestBodyBuilder()


class SearchCalendarEventRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._search_calendar_event_request_body = SearchCalendarEventRequestBody()

    def query(self, query: str) -> "SearchCalendarEventRequestBodyBuilder":
        self._search_calendar_event_request_body.query = query
        return self

    def filter(self, filter: EventSearchFilter) -> "SearchCalendarEventRequestBodyBuilder":
        self._search_calendar_event_request_body.filter = filter
        return self

    def build(self) -> "SearchCalendarEventRequestBody":
        return self._search_calendar_event_request_body
