# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .read_user import ReadUser


class ReadUsersMessageResponseBody(object):
    _types = {
        "items": List[ReadUser],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d):
        self.items: Optional[List[ReadUser]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ReadUsersMessageResponseBodyBuilder":
        return ReadUsersMessageResponseBodyBuilder()


class ReadUsersMessageResponseBodyBuilder(object):
    def __init__(self, read_users_message_response_body: ReadUsersMessageResponseBody = ReadUsersMessageResponseBody({})) -> None:
        self._read_users_message_response_body: ReadUsersMessageResponseBody = read_users_message_response_body
    
    def items(self, items: List[ReadUser]) -> "ReadUsersMessageResponseBodyBuilder":
        self._read_users_message_response_body.items = items
        return self
    
    def has_more(self, has_more: bool) -> "ReadUsersMessageResponseBodyBuilder":
        self._read_users_message_response_body.has_more = has_more
        return self
    
    def page_token(self, page_token: str) -> "ReadUsersMessageResponseBodyBuilder":
        self._read_users_message_response_body.page_token = page_token
        return self
    
    def build(self) -> "ReadUsersMessageResponseBody":
        return self._read_users_message_response_body