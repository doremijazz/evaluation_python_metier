from dataclasses import field, dataclass
from typing import ClassVar

from models.Book import Book
from models.User import User

@dataclass
class Member(User):
    member_id: ClassVar[int] = 0
    member_nbr: int = field(init=False)

    def display(self):
        person_str = super().__str__()
        print(f"Member_ID : {self.member_id}, Information : {person_str}")


    def vote(self,books:list[Book], nbr: int)-> list[Book]:
        selected_books = []
        while nbr > 0:
            for book in books:
                print(book.id)
                print(book)
            id_book = input("Saisir l'ID du livre")
            id_book = int(id_book)
            selected_books.append(book for book in books if book.id == id_book)
            nbr -= 1
            books.remove(book)
        return selected_books

