"""Modèle métier d'un livre sélectionné pour le prix."""

from dataclasses import field, dataclass
from typing import ClassVar

from models import Author
from datetime import date

@dataclass
class Book:
    """Regrouper les informations bibliographiques et commerciales d'un livre."""

    id :  ClassVar[int] = 0
    book_nbr : int = field(init=False)
    title: str
    author: Author
    resume: str
    publish_date: date
    editeur : str
    pp : list[str]
    nb_pages : int
    isbn : str
    price : float

    def __post_init__(self):
        """Attribuer un numéro local au livre après son initialisation."""

        Book.id += 1
        self.book_nbr = Book.id

    def __str__(self):
        """Retourner une présentation synthétique du livre."""

        return  (f"{self.title} by {self.author} editing by {self.editeur} published on {self.publish_date},\n"
                 f" nombre de pages {self.nb_pages}, isbn {self.isbn}, price {self.price}")

    @staticmethod
    def display_all_books(books:list["Book"]):
        """Afficher le titre et l'auteur de chaque livre fourni.

        Args:
            books: Livres à afficher.
        """
        for book in books:
            print(f"{book.title} by {book.author}")

    def display_resume(self):
        """Afficher le résumé du livre."""

        print(f"resume {self.resume}")