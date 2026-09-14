from dataclasses import field, dataclass
from typing import ClassVar

from models.Book import Book
from models.User import User

@dataclass
class Member(User):
    def __init__(self,username:str,password:str,email:str):
        super().__init__(username,password,email)
        member_id: ClassVar[int] = 0
        member_nbr: int = field(init=False)

    def vote(self,books:list[Book]):
        pass