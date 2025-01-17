# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .application_feedback import ApplicationFeedback


class ListApplicationFeedbackResponseBody(object):
    _types = {
        "feedback_list": List[ApplicationFeedback],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d=None):
        self.feedback_list: Optional[List[ApplicationFeedback]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListApplicationFeedbackResponseBodyBuilder":
        return ListApplicationFeedbackResponseBodyBuilder()


class ListApplicationFeedbackResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_application_feedback_response_body = ListApplicationFeedbackResponseBody()

    def feedback_list(self, feedback_list: List[ApplicationFeedback]) -> "ListApplicationFeedbackResponseBodyBuilder":
        self._list_application_feedback_response_body.feedback_list = feedback_list
        return self

    def has_more(self, has_more: bool) -> "ListApplicationFeedbackResponseBodyBuilder":
        self._list_application_feedback_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListApplicationFeedbackResponseBodyBuilder":
        self._list_application_feedback_response_body.page_token = page_token
        return self

    def build(self) -> "ListApplicationFeedbackResponseBody":
        return self._list_application_feedback_response_body
