from typing import ClassVar

from models import Author
from datetime import date


class Book:
    id :  ClassVar[int] = 0
    title: str
    author: Author
    resume: str
    publish_date: date
    editeur : str
    pp : list[str]
    nb_pages : int
    isbn : int
    price : float

    def _post_init__(self):
        self.id +=1

    def _str_(self):
        return  (f"{self.title} by {self.author} editing by {self.editeur} published on {self.publish_date},\n"
                 f" nombre de pages {self.nb_pages}, isbn {self.isbn}, price {self.price}")

    def display_all_books(list:list[Book]):
        for book in list:
            print(f"{book.title} by {book.author}")

    def display_resume(self):
        print(f"resume {self.resume}")