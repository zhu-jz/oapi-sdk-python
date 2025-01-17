# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .id_name_object import IdNameObject
from .interview_dimension_assessment import InterviewDimensionAssessment
from .interview_score import InterviewScore


class InterviewRecord(object):
    _types = {
        "id": str,
        "user_id": str,
        "content": str,
        "min_job_level_id": str,
        "max_job_level_id": str,
        "commit_status": int,
        "feedback_submit_time": int,
        "conclusion": int,
        "interview_score": InterviewScore,
        "interviewer": IdNameObject,
        "dimension_assessment_list": List[InterviewDimensionAssessment],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.user_id: Optional[str] = None
        self.content: Optional[str] = None
        self.min_job_level_id: Optional[str] = None
        self.max_job_level_id: Optional[str] = None
        self.commit_status: Optional[int] = None
        self.feedback_submit_time: Optional[int] = None
        self.conclusion: Optional[int] = None
        self.interview_score: Optional[InterviewScore] = None
        self.interviewer: Optional[IdNameObject] = None
        self.dimension_assessment_list: Optional[List[InterviewDimensionAssessment]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InterviewRecordBuilder":
        return InterviewRecordBuilder()


class InterviewRecordBuilder(object):
    def __init__(self) -> None:
        self._interview_record = InterviewRecord()

    def id(self, id: str) -> "InterviewRecordBuilder":
        self._interview_record.id = id
        return self

    def user_id(self, user_id: str) -> "InterviewRecordBuilder":
        self._interview_record.user_id = user_id
        return self

    def content(self, content: str) -> "InterviewRecordBuilder":
        self._interview_record.content = content
        return self

    def min_job_level_id(self, min_job_level_id: str) -> "InterviewRecordBuilder":
        self._interview_record.min_job_level_id = min_job_level_id
        return self

    def max_job_level_id(self, max_job_level_id: str) -> "InterviewRecordBuilder":
        self._interview_record.max_job_level_id = max_job_level_id
        return self

    def commit_status(self, commit_status: int) -> "InterviewRecordBuilder":
        self._interview_record.commit_status = commit_status
        return self

    def feedback_submit_time(self, feedback_submit_time: int) -> "InterviewRecordBuilder":
        self._interview_record.feedback_submit_time = feedback_submit_time
        return self

    def conclusion(self, conclusion: int) -> "InterviewRecordBuilder":
        self._interview_record.conclusion = conclusion
        return self

    def interview_score(self, interview_score: InterviewScore) -> "InterviewRecordBuilder":
        self._interview_record.interview_score = interview_score
        return self

    def interviewer(self, interviewer: IdNameObject) -> "InterviewRecordBuilder":
        self._interview_record.interviewer = interviewer
        return self

    def dimension_assessment_list(self, dimension_assessment_list: List[
        InterviewDimensionAssessment]) -> "InterviewRecordBuilder":
        self._interview_record.dimension_assessment_list = dimension_assessment_list
        return self

    def build(self) -> "InterviewRecord":
        return self._interview_record
