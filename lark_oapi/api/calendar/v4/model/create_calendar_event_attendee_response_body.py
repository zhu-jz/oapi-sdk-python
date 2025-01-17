# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .calendar_event_attendee import CalendarEventAttendee


class CreateCalendarEventAttendeeResponseBody(object):
    _types = {
        "attendees": List[CalendarEventAttendee],
    }

    def __init__(self, d=None):
        self.attendees: Optional[List[CalendarEventAttendee]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateCalendarEventAttendeeResponseBodyBuilder":
        return CreateCalendarEventAttendeeResponseBodyBuilder()


class CreateCalendarEventAttendeeResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_calendar_event_attendee_response_body = CreateCalendarEventAttendeeResponseBody()

    def attendees(self, attendees: List[CalendarEventAttendee]) -> "CreateCalendarEventAttendeeResponseBodyBuilder":
        self._create_calendar_event_attendee_response_body.attendees = attendees
        return self

    def build(self) -> "CreateCalendarEventAttendeeResponseBody":
        return self._create_calendar_event_attendee_response_body
