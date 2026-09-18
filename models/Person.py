# -*- coding: utf-8 -*-

"""
Classe abstraite Person, mère de Student et Teacher
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class Person(ABC):
    """Person liée au concours : président ou membre ou auteur"""
    id_person: ClassVar[int] = 0
    person_nbr:  int = field(init=False)
    first_name: str
    last_name: str
    age: int

    @abstractmethod
    def display(self):
        """Afficher les informations de la personne dans la console."""

        pass

    def __str__(self):
        """Retourner l'identité de la personne."""

        return f"{self.first_name} {self.last_name}, {self.age} ans"