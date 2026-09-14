from dataclasses import field, dataclass
from typing import ClassVar

from models.Book import Book
from models.User import User

@dataclass
class Member(User):
    member_id: ClassVar[int] = 0
    member_nbr: int = field(init=False)
    def __post_init__(self):
        self.member_id = self.member_id+1
        self.member_nbr = self.member_id


    def vote(self,books:list[Book]):
        pass