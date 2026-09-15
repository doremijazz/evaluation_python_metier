from dataclasses import dataclass
from typing import Optional

from daos.dao import Dao
from models.Member import Member


@dataclass
class MemberDao(Dao[Member]):
    def create(self, member: Member) -> int:
        pass
    def read(self, member_id: int) -> Member:
        pass
    def readAll(self) -> list[Member]:
        pass
    def update(self, member: Member) -> bool:
        pass
    def delete(self, member: Member) -> bool:
        pass
