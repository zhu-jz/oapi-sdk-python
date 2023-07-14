# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .calendar_event import CalendarEvent


class PatchCalendarEventResponseBody(object):
    _types = {
        "event": CalendarEvent,
    }

    def __init__(self, d):
        self.event: Optional[CalendarEvent] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchCalendarEventResponseBodyBuilder":
        return PatchCalendarEventResponseBodyBuilder()


class PatchCalendarEventResponseBodyBuilder(object):
    def __init__(self, patch_calendar_event_response_body: PatchCalendarEventResponseBody = PatchCalendarEventResponseBody({})) -> None:
        self._patch_calendar_event_response_body: PatchCalendarEventResponseBody = patch_calendar_event_response_body
    
    def event(self, event: CalendarEvent) -> "PatchCalendarEventResponseBodyBuilder":
        self._patch_calendar_event_response_body.event = event
        return self
    
    def build(self) -> "PatchCalendarEventResponseBody":
        return self._patch_calendar_event_response_body