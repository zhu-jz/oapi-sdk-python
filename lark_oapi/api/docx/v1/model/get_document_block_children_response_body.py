# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .block import Block


class GetDocumentBlockChildrenResponseBody(object):
    _types = {
        "items": List[Block],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[Block]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetDocumentBlockChildrenResponseBodyBuilder":
        return GetDocumentBlockChildrenResponseBodyBuilder()


class GetDocumentBlockChildrenResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_document_block_children_response_body = GetDocumentBlockChildrenResponseBody()

    def items(self, items: List[Block]) -> "GetDocumentBlockChildrenResponseBodyBuilder":
        self._get_document_block_children_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "GetDocumentBlockChildrenResponseBodyBuilder":
        self._get_document_block_children_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "GetDocumentBlockChildrenResponseBodyBuilder":
        self._get_document_block_children_response_body.has_more = has_more
        return self

    def build(self) -> "GetDocumentBlockChildrenResponseBody":
        return self._get_document_block_children_response_body
