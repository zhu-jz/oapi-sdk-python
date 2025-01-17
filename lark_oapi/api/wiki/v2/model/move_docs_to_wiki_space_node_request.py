# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .move_docs_to_wiki_space_node_request_body import MoveDocsToWikiSpaceNodeRequestBody


class MoveDocsToWikiSpaceNodeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.space_id: Optional[int] = None
        self.request_body: Optional[MoveDocsToWikiSpaceNodeRequestBody] = None

    @staticmethod
    def builder() -> "MoveDocsToWikiSpaceNodeRequestBuilder":
        return MoveDocsToWikiSpaceNodeRequestBuilder()


class MoveDocsToWikiSpaceNodeRequestBuilder(object):

    def __init__(self) -> None:
        move_docs_to_wiki_space_node_request = MoveDocsToWikiSpaceNodeRequest()
        move_docs_to_wiki_space_node_request.http_method = HttpMethod.POST
        move_docs_to_wiki_space_node_request.uri = "/open-apis/wiki/v2/spaces/:space_id/nodes/move_docs_to_wiki"
        move_docs_to_wiki_space_node_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._move_docs_to_wiki_space_node_request: MoveDocsToWikiSpaceNodeRequest = move_docs_to_wiki_space_node_request

    def space_id(self, space_id: int) -> "MoveDocsToWikiSpaceNodeRequestBuilder":
        self._move_docs_to_wiki_space_node_request.space_id = space_id
        self._move_docs_to_wiki_space_node_request.paths["space_id"] = str(space_id)
        return self

    def request_body(self, request_body: MoveDocsToWikiSpaceNodeRequestBody) -> "MoveDocsToWikiSpaceNodeRequestBuilder":
        self._move_docs_to_wiki_space_node_request.request_body = request_body
        self._move_docs_to_wiki_space_node_request.body = request_body
        return self

    def build(self) -> MoveDocsToWikiSpaceNodeRequest:
        return self._move_docs_to_wiki_space_node_request
