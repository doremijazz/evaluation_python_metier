from dataclasses import dataclass
from typing import Optional

from daos.dao import Dao
from models.Book import Book


@dataclass
class MemberDao(Dao[Book]):
    def create(self, book: Book) -> int:
        pass
    def read(self, book_id: int) -> Book:
        pass
    def readAll(self) -> list[Book]:
        pass
    def update(self, book: Book) -> bool:
        pass
    def delete(self, book: Book) -> bool:
        pass