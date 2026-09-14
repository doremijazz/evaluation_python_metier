# -*- coding: utf-8 -*-

"""
Classe goncourt
"""

from dataclasses import dataclass, field
from datetime import date
from typing import Optional


from models.User import User
from models.Author import Author
from models.Book import Book
from models.Member import Member


@dataclass
class goncourt:
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
    president: User = field(default_factory=User, init=False)