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



    def enter_vote(books : list[Book]) -> list[Book]:
        book_votes = dict
        book_selec = list[Book]
        for book in books:
            print(book)
            vote = input("Saisie le nombre de vote")
            book_votes[book] = book_votes.get(book, vote) + 1
        book_votes = dict(sorted(book_votes.items(), key=lambda item: item[1], reverse=True))
        for book in book_votes:
            book_selec.append(book_votes[book])
        return book_selec

    def announce_vote(books : list[Book], nb : int) -> list[Book]:
        book_announce = list[Book]
        while len(book_announce) < nb:
            for book in books:
                choice = input("Saisie le choix de vote o/n")
                if choice == "o":
                    book_announce.append(book)
        return book_announce