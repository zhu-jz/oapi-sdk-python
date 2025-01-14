# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class TalentFolder(object):
    _types = {
        "external_id": str,
        "name": str,
        "parent_id": str,
        "creator_id": str,
        "folder_id": str,
        "owner_id": str,
    }

    def __init__(self, d=None):
        self.external_id: Optional[str] = None
        self.name: Optional[str] = None
        self.parent_id: Optional[str] = None
        self.creator_id: Optional[str] = None
        self.folder_id: Optional[str] = None
        self.owner_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TalentFolderBuilder":
        return TalentFolderBuilder()


class TalentFolderBuilder(object):
    def __init__(self) -> None:
        self._talent_folder = TalentFolder()

    def external_id(self, external_id: str) -> "TalentFolderBuilder":
        self._talent_folder.external_id = external_id
        return self

    def name(self, name: str) -> "TalentFolderBuilder":
        self._talent_folder.name = name
        return self

    def parent_id(self, parent_id: str) -> "TalentFolderBuilder":
        self._talent_folder.parent_id = parent_id
        return self

    def creator_id(self, creator_id: str) -> "TalentFolderBuilder":
        self._talent_folder.creator_id = creator_id
        return self

    def folder_id(self, folder_id: str) -> "TalentFolderBuilder":
        self._talent_folder.folder_id = folder_id
        return self

    def owner_id(self, owner_id: str) -> "TalentFolderBuilder":
        self._talent_folder.owner_id = owner_id
        return self

    def build(self) -> "TalentFolder":
        return self._talent_folder
