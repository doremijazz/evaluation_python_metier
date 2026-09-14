from dataclasses import dataclass, field
from typing import ClassVar

from models.Book import Book
from models.User import User

@dataclass
class president(User):
    def __init__(self,username:str,password:str,email:str):
        super().__init__(username,password,email)

    def display(self):
        pass

    def enter_vote(self) -> list[Book]:
        pass

    def announce_vote(books : list[Book]):
        pass