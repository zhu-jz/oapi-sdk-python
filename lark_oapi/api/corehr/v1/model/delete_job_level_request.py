# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteJobLevelRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.job_level_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteJobLevelRequestBuilder":
        return DeleteJobLevelRequestBuilder()


class DeleteJobLevelRequestBuilder(object):

    def __init__(self) -> None:
        delete_job_level_request = DeleteJobLevelRequest()
        delete_job_level_request.http_method = HttpMethod.DELETE
        delete_job_level_request.uri = "/open-apis/corehr/v1/job_levels/:job_level_id"
        delete_job_level_request.token_types = {AccessTokenType.TENANT}
        self._delete_job_level_request: DeleteJobLevelRequest = delete_job_level_request

    def job_level_id(self, job_level_id: str) -> "DeleteJobLevelRequestBuilder":
        self._delete_job_level_request.job_level_id = job_level_id
        self._delete_job_level_request.paths["job_level_id"] = str(job_level_id)
        return self

    def build(self) -> DeleteJobLevelRequest:
        return self._delete_job_level_request
