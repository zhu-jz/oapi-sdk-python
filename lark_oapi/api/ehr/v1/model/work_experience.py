# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class WorkExperience(object):
    _types = {
        "company": str,
        "department": str,
        "job": str,
        "start": str,
        "end": str,
        "description": str,
    }

    def __init__(self, d=None):
        self.company: Optional[str] = None
        self.department: Optional[str] = None
        self.job: Optional[str] = None
        self.start: Optional[str] = None
        self.end: Optional[str] = None
        self.description: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WorkExperienceBuilder":
        return WorkExperienceBuilder()


class WorkExperienceBuilder(object):
    def __init__(self) -> None:
        self._work_experience = WorkExperience()

    def company(self, company: str) -> "WorkExperienceBuilder":
        self._work_experience.company = company
        return self

    def department(self, department: str) -> "WorkExperienceBuilder":
        self._work_experience.department = department
        return self

    def job(self, job: str) -> "WorkExperienceBuilder":
        self._work_experience.job = job
        return self

    def start(self, start: str) -> "WorkExperienceBuilder":
        self._work_experience.start = start
        return self

    def end(self, end: str) -> "WorkExperienceBuilder":
        self._work_experience.end = end
        return self

    def description(self, description: str) -> "WorkExperienceBuilder":
        self._work_experience.description = description
        return self

    def build(self) -> "WorkExperience":
        return self._work_experience
