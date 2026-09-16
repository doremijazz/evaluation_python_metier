from dataclasses import dataclass
from typing import Optional

from daos.dao import Dao
from models.User import User


@dataclass
class UserDao(Dao[User]):
    def create(self, user: User) -> int:
        pass
    def read(self, user_id: int) -> User:
        pass
    def readAll(self) -> list[User]:
        pass
    def update(self, user: User) -> bool:
        pass
    def delete(self, user: User) -> bool:
        pass