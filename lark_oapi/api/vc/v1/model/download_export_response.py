# Code generated by Lark OpenAPI.

from typing import *
from typing import IO

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse


class DownloadExportResponse(BaseResponse):
    _types = {
        "file": IO[Any],
        "file_name": str,
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.file: Optional[IO[Any]] = None
        self.file_name: Optional[str] = None
        init(self, d, self._types)
