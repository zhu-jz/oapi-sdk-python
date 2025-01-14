# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CreateTimeoffEventResponseBody(object):
    _types = {
        "timeoff_event_id": str,
        "user_id": str,
        "timezone": str,
        "start_time": str,
        "end_time": str,
        "title": str,
        "description": str,
    }

    def __init__(self, d=None):
        self.timeoff_event_id: Optional[str] = None
        self.user_id: Optional[str] = None
        self.timezone: Optional[str] = None
        self.start_time: Optional[str] = None
        self.end_time: Optional[str] = None
        self.title: Optional[str] = None
        self.description: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateTimeoffEventResponseBodyBuilder":
        return CreateTimeoffEventResponseBodyBuilder()


class CreateTimeoffEventResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_timeoff_event_response_body = CreateTimeoffEventResponseBody()

    def timeoff_event_id(self, timeoff_event_id: str) -> "CreateTimeoffEventResponseBodyBuilder":
        self._create_timeoff_event_response_body.timeoff_event_id = timeoff_event_id
        return self

    def user_id(self, user_id: str) -> "CreateTimeoffEventResponseBodyBuilder":
        self._create_timeoff_event_response_body.user_id = user_id
        return self

    def timezone(self, timezone: str) -> "CreateTimeoffEventResponseBodyBuilder":
        self._create_timeoff_event_response_body.timezone = timezone
        return self

    def start_time(self, start_time: str) -> "CreateTimeoffEventResponseBodyBuilder":
        self._create_timeoff_event_response_body.start_time = start_time
        return self

    def end_time(self, end_time: str) -> "CreateTimeoffEventResponseBodyBuilder":
        self._create_timeoff_event_response_body.end_time = end_time
        return self

    def title(self, title: str) -> "CreateTimeoffEventResponseBodyBuilder":
        self._create_timeoff_event_response_body.title = title
        return self

    def description(self, description: str) -> "CreateTimeoffEventResponseBodyBuilder":
        self._create_timeoff_event_response_body.description = description
        return self

    def build(self) -> "CreateTimeoffEventResponseBody":
        return self._create_timeoff_event_response_body
