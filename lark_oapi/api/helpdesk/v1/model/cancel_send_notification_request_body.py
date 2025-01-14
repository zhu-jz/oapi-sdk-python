# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class CancelSendNotificationRequestBody(object):
    _types = {
        "is_recall": bool,
    }

    def __init__(self, d=None):
        self.is_recall: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CancelSendNotificationRequestBodyBuilder":
        return CancelSendNotificationRequestBodyBuilder()


class CancelSendNotificationRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._cancel_send_notification_request_body = CancelSendNotificationRequestBody()

    def is_recall(self, is_recall: bool) -> "CancelSendNotificationRequestBodyBuilder":
        self._cancel_send_notification_request_body.is_recall = is_recall
        return self

    def build(self) -> "CancelSendNotificationRequestBody":
        return self._cancel_send_notification_request_body
