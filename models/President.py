from dataclasses import dataclass, field
from typing import ClassVar

from models.Book import Book
from models.User import User

@dataclass
class President(User):

    def display(self):
        print(f" ID: {self.user_id}")
        print(f" Surname: {self.last_name}")
        print(f" Name: {self.first_name}")
        print(f" Email: {self.email}")

    @staticmethod
    def announce_vote(books : list[Book], nb : int) -> list[Book]:
        book_announce = []
        while len(book_announce) < nb:
            for book in books:
                print(book)
                choice = input("Saisie le choix de vote o/n")
                if choice == "o":
                    book_announce.append(book)
        return book_announce

    @staticmethod
    def enter_vote(books: list[Book]) -> list[Book]:
        print(f"Nombre de livres : {len(books)}")
        book_votes = {}

        # Collect votes with validation
        for book in books:
            print(book)
            while True:
                try:
                    vote = int(input("Saisir le nombre de votes : "))
                    if vote < 0:
                        print("Le nombre de votes ne peut pas être négatif.")
                        continue
                    break
                except ValueError:
                    print("Veuillez entrer un nombre entier valide.")
            book_votes[book.id] = vote

        # Sort by votes (descending)
        sorted_books = sorted(
            books,
            key=lambda b: book_votes[b.id],
            reverse=True
        )

        return sorted_books