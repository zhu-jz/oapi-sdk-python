# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetMeetingRecordingRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.meeting_id: Optional[int] = None

    @staticmethod
    def builder() -> "GetMeetingRecordingRequestBuilder":
        return GetMeetingRecordingRequestBuilder()


class GetMeetingRecordingRequestBuilder(object):

    def __init__(self, get_meeting_recording_request: GetMeetingRecordingRequest = GetMeetingRecordingRequest()) -> None:
        get_meeting_recording_request.http_method = HttpMethod.GET
        get_meeting_recording_request.uri = "/open-apis/vc/v1/meetings/:meeting_id/recording"
        get_meeting_recording_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._get_meeting_recording_request: GetMeetingRecordingRequest = get_meeting_recording_request
    
    def meeting_id(self, meeting_id: int) -> "GetMeetingRecordingRequestBuilder":
        self._get_meeting_recording_request.meeting_id = meeting_id
        self._get_meeting_recording_request.paths["meeting_id"] = meeting_id
        return self
    

    def build(self) -> GetMeetingRecordingRequest:
        return self._get_meeting_recording_request