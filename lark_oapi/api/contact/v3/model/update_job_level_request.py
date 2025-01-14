# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .job_level import JobLevel


class UpdateJobLevelRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.job_level_id: Optional[str] = None
        self.request_body: Optional[JobLevel] = None

    @staticmethod
    def builder() -> "UpdateJobLevelRequestBuilder":
        return UpdateJobLevelRequestBuilder()


class UpdateJobLevelRequestBuilder(object):

    def __init__(self) -> None:
        update_job_level_request = UpdateJobLevelRequest()
        update_job_level_request.http_method = HttpMethod.PUT
        update_job_level_request.uri = "/open-apis/contact/v3/job_levels/:job_level_id"
        update_job_level_request.token_types = {AccessTokenType.TENANT}
        self._update_job_level_request: UpdateJobLevelRequest = update_job_level_request

    def job_level_id(self, job_level_id: str) -> "UpdateJobLevelRequestBuilder":
        self._update_job_level_request.job_level_id = job_level_id
        self._update_job_level_request.paths["job_level_id"] = str(job_level_id)
        return self

    def request_body(self, request_body: JobLevel) -> "UpdateJobLevelRequestBuilder":
        self._update_job_level_request.request_body = request_body
        self._update_job_level_request.body = request_body
        return self

    def build(self) -> UpdateJobLevelRequest:
        return self._update_job_level_request
