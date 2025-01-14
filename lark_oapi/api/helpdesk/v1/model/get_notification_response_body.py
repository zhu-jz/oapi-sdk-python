# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .notification import Notification


class GetNotificationResponseBody(object):
    _types = {
        "notification": Notification,
        "approval_app_link": str,
    }

    def __init__(self, d=None):
        self.notification: Optional[Notification] = None
        self.approval_app_link: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetNotificationResponseBodyBuilder":
        return GetNotificationResponseBodyBuilder()


class GetNotificationResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_notification_response_body = GetNotificationResponseBody()

    def notification(self, notification: Notification) -> "GetNotificationResponseBodyBuilder":
        self._get_notification_response_body.notification = notification
        return self

    def approval_app_link(self, approval_app_link: str) -> "GetNotificationResponseBodyBuilder":
        self._get_notification_response_body.approval_app_link = approval_app_link
        return self

    def build(self) -> "GetNotificationResponseBody":
        return self._get_notification_response_body
