"""Modèle d'un membre du jury et comportement de vote."""

from dataclasses import field, dataclass
from typing import ClassVar

from models.Book import Book
from models.User import User

@dataclass
class Member(User):
    """Représenter un juré autorisé à sélectionner des livres."""

    member_id: ClassVar[int] = 0
    member_nbr: int = field(init=False)

    def __post_init__(self):
        """Initialiser l'utilisateur puis attribuer son numéro de membre."""

        super().__post_init__()
        Member.member_id += 1
        self.member_nbr = Member.member_id

    def display(self):
        """Afficher l'identifiant et les informations du membre."""

        person_str = super().__str__()
        print(f"Member_ID : {self.member_nbr}, \nInformation : {person_str}")

    @staticmethod
    def vote(books:list[Book], nbr: int)-> list[Book]:
        """Demander au membre de choisir un nombre donné de livres.

        Args:
            books: Livres parmi lesquels effectuer la sélection.
            nbr: Nombre de livres à retenir.

        Returns:
            Liste des livres choisis par le membre.
        """
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

