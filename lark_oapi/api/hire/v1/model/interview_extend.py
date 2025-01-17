# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .code_name_object import CodeNameObject
from .id_name_object import IdNameObject
from .interview_address import InterviewAddress
from .interview_meeting_room import InterviewMeetingRoom
from .interview_record import InterviewRecord


class InterviewExtend(object):
    _types = {
        "id": str,
        "begin_time": int,
        "end_time": int,
        "round": int,
        "interview_record_list": List[InterviewRecord],
        "feedback_submit_time": int,
        "stage_id": str,
        "application_id": str,
        "stage": IdNameObject,
        "creator": IdNameObject,
        "biz_create_time": int,
        "biz_modify_time": int,
        "interview_round_summary": int,
        "interview_arrangement_id": str,
        "interview_type": int,
        "talent_time_zone": CodeNameObject,
        "contact_user": IdNameObject,
        "contact_mobile": str,
        "remark": str,
        "address": InterviewAddress,
        "video_type": int,
        "arrangement_status": int,
        "arrangement_type": int,
        "arrangement_appointment_kind": int,
        "meeting_room_list": List[InterviewMeetingRoom],
        "interview_round_type": IdNameObject,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.begin_time: Optional[int] = None
        self.end_time: Optional[int] = None
        self.round: Optional[int] = None
        self.interview_record_list: Optional[List[InterviewRecord]] = None
        self.feedback_submit_time: Optional[int] = None
        self.stage_id: Optional[str] = None
        self.application_id: Optional[str] = None
        self.stage: Optional[IdNameObject] = None
        self.creator: Optional[IdNameObject] = None
        self.biz_create_time: Optional[int] = None
        self.biz_modify_time: Optional[int] = None
        self.interview_round_summary: Optional[int] = None
        self.interview_arrangement_id: Optional[str] = None
        self.interview_type: Optional[int] = None
        self.talent_time_zone: Optional[CodeNameObject] = None
        self.contact_user: Optional[IdNameObject] = None
        self.contact_mobile: Optional[str] = None
        self.remark: Optional[str] = None
        self.address: Optional[InterviewAddress] = None
        self.video_type: Optional[int] = None
        self.arrangement_status: Optional[int] = None
        self.arrangement_type: Optional[int] = None
        self.arrangement_appointment_kind: Optional[int] = None
        self.meeting_room_list: Optional[List[InterviewMeetingRoom]] = None
        self.interview_round_type: Optional[IdNameObject] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InterviewExtendBuilder":
        return InterviewExtendBuilder()


class InterviewExtendBuilder(object):
    def __init__(self) -> None:
        self._interview_extend = InterviewExtend()

    def id(self, id: str) -> "InterviewExtendBuilder":
        self._interview_extend.id = id
        return self

    def begin_time(self, begin_time: int) -> "InterviewExtendBuilder":
        self._interview_extend.begin_time = begin_time
        return self

    def end_time(self, end_time: int) -> "InterviewExtendBuilder":
        self._interview_extend.end_time = end_time
        return self

    def round(self, round: int) -> "InterviewExtendBuilder":
        self._interview_extend.round = round
        return self

    def interview_record_list(self, interview_record_list: List[InterviewRecord]) -> "InterviewExtendBuilder":
        self._interview_extend.interview_record_list = interview_record_list
        return self

    def feedback_submit_time(self, feedback_submit_time: int) -> "InterviewExtendBuilder":
        self._interview_extend.feedback_submit_time = feedback_submit_time
        return self

    def stage_id(self, stage_id: str) -> "InterviewExtendBuilder":
        self._interview_extend.stage_id = stage_id
        return self

    def application_id(self, application_id: str) -> "InterviewExtendBuilder":
        self._interview_extend.application_id = application_id
        return self

    def stage(self, stage: IdNameObject) -> "InterviewExtendBuilder":
        self._interview_extend.stage = stage
        return self

    def creator(self, creator: IdNameObject) -> "InterviewExtendBuilder":
        self._interview_extend.creator = creator
        return self

    def biz_create_time(self, biz_create_time: int) -> "InterviewExtendBuilder":
        self._interview_extend.biz_create_time = biz_create_time
        return self

    def biz_modify_time(self, biz_modify_time: int) -> "InterviewExtendBuilder":
        self._interview_extend.biz_modify_time = biz_modify_time
        return self

    def interview_round_summary(self, interview_round_summary: int) -> "InterviewExtendBuilder":
        self._interview_extend.interview_round_summary = interview_round_summary
        return self

    def interview_arrangement_id(self, interview_arrangement_id: str) -> "InterviewExtendBuilder":
        self._interview_extend.interview_arrangement_id = interview_arrangement_id
        return self

    def interview_type(self, interview_type: int) -> "InterviewExtendBuilder":
        self._interview_extend.interview_type = interview_type
        return self

    def talent_time_zone(self, talent_time_zone: CodeNameObject) -> "InterviewExtendBuilder":
        self._interview_extend.talent_time_zone = talent_time_zone
        return self

    def contact_user(self, contact_user: IdNameObject) -> "InterviewExtendBuilder":
        self._interview_extend.contact_user = contact_user
        return self

    def contact_mobile(self, contact_mobile: str) -> "InterviewExtendBuilder":
        self._interview_extend.contact_mobile = contact_mobile
        return self

    def remark(self, remark: str) -> "InterviewExtendBuilder":
        self._interview_extend.remark = remark
        return self

    def address(self, address: InterviewAddress) -> "InterviewExtendBuilder":
        self._interview_extend.address = address
        return self

    def video_type(self, video_type: int) -> "InterviewExtendBuilder":
        self._interview_extend.video_type = video_type
        return self

    def arrangement_status(self, arrangement_status: int) -> "InterviewExtendBuilder":
        self._interview_extend.arrangement_status = arrangement_status
        return self

    def arrangement_type(self, arrangement_type: int) -> "InterviewExtendBuilder":
        self._interview_extend.arrangement_type = arrangement_type
        return self

    def arrangement_appointment_kind(self, arrangement_appointment_kind: int) -> "InterviewExtendBuilder":
        self._interview_extend.arrangement_appointment_kind = arrangement_appointment_kind
        return self

    def meeting_room_list(self, meeting_room_list: List[InterviewMeetingRoom]) -> "InterviewExtendBuilder":
        self._interview_extend.meeting_room_list = meeting_room_list
        return self

    def interview_round_type(self, interview_round_type: IdNameObject) -> "InterviewExtendBuilder":
        self._interview_extend.interview_round_type = interview_round_type
        return self

    def build(self) -> "InterviewExtend":
        return self._interview_extend
