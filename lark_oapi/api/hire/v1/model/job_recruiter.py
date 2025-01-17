# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class JobRecruiter(object):
    _types = {
        "id": str,
        "recruiter_id": str,
        "hiring_manager_id_list": List[str],
        "assistant_id_list": List[str],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.recruiter_id: Optional[str] = None
        self.hiring_manager_id_list: Optional[List[str]] = None
        self.assistant_id_list: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobRecruiterBuilder":
        return JobRecruiterBuilder()


class JobRecruiterBuilder(object):
    def __init__(self) -> None:
        self._job_recruiter = JobRecruiter()

    def id(self, id: str) -> "JobRecruiterBuilder":
        self._job_recruiter.id = id
        return self

    def recruiter_id(self, recruiter_id: str) -> "JobRecruiterBuilder":
        self._job_recruiter.recruiter_id = recruiter_id
        return self

    def hiring_manager_id_list(self, hiring_manager_id_list: List[str]) -> "JobRecruiterBuilder":
        self._job_recruiter.hiring_manager_id_list = hiring_manager_id_list
        return self

    def assistant_id_list(self, assistant_id_list: List[str]) -> "JobRecruiterBuilder":
        self._job_recruiter.assistant_id_list = assistant_id_list
        return self

    def build(self) -> "JobRecruiter":
        return self._job_recruiter
