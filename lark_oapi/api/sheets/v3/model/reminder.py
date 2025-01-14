# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Reminder(object):
    _types = {
        "notify_date_time": str,
        "notify_user_id": List[str],
        "notify_text": str,
        "notify_strategy": str,
    }

    def __init__(self, d=None):
        self.notify_date_time: Optional[str] = None
        self.notify_user_id: Optional[List[str]] = None
        self.notify_text: Optional[str] = None
        self.notify_strategy: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReminderBuilder":
        return ReminderBuilder()


class ReminderBuilder(object):
    def __init__(self) -> None:
        self._reminder = Reminder()

    def notify_date_time(self, notify_date_time: str) -> "ReminderBuilder":
        self._reminder.notify_date_time = notify_date_time
        return self

    def notify_user_id(self, notify_user_id: List[str]) -> "ReminderBuilder":
        self._reminder.notify_user_id = notify_user_id
        return self

    def notify_text(self, notify_text: str) -> "ReminderBuilder":
        self._reminder.notify_text = notify_text
        return self

    def notify_strategy(self, notify_strategy: str) -> "ReminderBuilder":
        self._reminder.notify_strategy = notify_strategy
        return self

    def build(self) -> "Reminder":
        return self._reminder
