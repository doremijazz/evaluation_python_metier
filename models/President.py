from dataclasses import dataclass, field
from typing import ClassVar

from models.Book import Book
from models.User import User


class president(User):

    def display(self):
        pass

    def enter_vote(self) -> list[Book]:
        pass

    def announce_vote(books : list[Book]):
        pass