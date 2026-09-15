from dataclasses import field, dataclass
from typing import ClassVar

from models import Author
from datetime import date

@dataclass
class Book:
    id :  ClassVar[int] = 0
    book_nbr : int = field(init=False)
    title: str
    author: Author
    resume: str
    publish_date: date
    editeur : str
    pp : list[str]
    nb_pages : int
    isbn : int
    price : float

    def __post_init__(self):
        Book.id += 1
        self.book_nbr = Book.id

    def __str__(self):
        return  (f"{self.title} by {self.author} editing by {self.editeur} published on {self.publish_date},\n"
                 f" nombre de pages {self.nb_pages}, isbn {self.isbn}, price {self.price}")

    @staticmethod
    def display_all_books(books:list["Book"]):
        for book in books:
            print(f"{book.title} by {book.author}")

    def display_resume(self):
        print(f"resume {self.resume}")