# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_task_collaborator_response_body import ListTaskCollaboratorResponseBody


class ListTaskCollaboratorResponse(BaseResponse):
    _types = {
        "data": ListTaskCollaboratorResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListTaskCollaboratorResponseBody] = None
        init(self, d, self._types)
