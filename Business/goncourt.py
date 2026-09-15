# -*- coding: utf-8 -*-

"""
Classe goncourt
"""

from dataclasses import dataclass, field
from datetime import date
from typing import Optional

from models.President import President
from models.User import User
from models.Author import Author
from models.Book import Book
from models.Member import Member


@dataclass
class Goncourt:
    """Couche metier de l'application de gestion du concours goncourt
    reprenant les cas d'utilisation et les spécifications fonctionnelles
    -book : liste des 16 livres prés selctioné
    -author : liste des auteurs
    -member : liste des membres
    -president : le president
    -user : liste des utilisateurs
    """
    book: list[Book] = field(default_factory=list, init=False)
    author: list[Author] = field(default_factory=list, init=False)
    member: list[Member] = field(default_factory=list, init=False)

    def add_book(self,book:Book):
        self.book.append(book)

    def add_author(self,author:Author):
        self.author.append(author)

    def add_member(self,member:Member):
        self.member.append(member)

    def init_static(self):
        """Initialisation du static de l'application de gestion"""
        president = President("Dedier", "DECOIN", 81, "dedier@gncourt.fr", "1234", "President")
        francoise : Member = Member("Francoise", "Chandernagor", 81, "francoise@goncourt.fr", "1234", "Member")
        tahar : Member = Member("Tahar Ben", "Jelloun", 81, "taharben@goncourt.fr", "1234", "Member")
        francoise.display()
