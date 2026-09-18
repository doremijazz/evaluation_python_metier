"""Modèle métier d'un auteur de livre."""

from dataclasses import dataclass, field
from typing import ClassVar

from models.Person import Person


@dataclass
class Author(Person):
    """Représenter un auteur et sa biographie."""

    author_id: ClassVar[int] = 0
    author_nbr: int = field(init=False)
    biography: str

    def __post_init__(self):
        """Attribuer un numéro local à la création de l'auteur."""

        Author.author_id +=1
        Author.author_nbr = self.author_id

    def display(self):
        """Afficher l'identité et la biographie de l'auteur."""

        person_str = super().__str__()
        print(f"{person_str}. \n Biographie : {self.biography}")

    def __str__(self):
        """Retourner l'identité et la biographie sous forme de texte."""

        person_str = super().__str__()
        return f"{person_str}. \n Biographie : {self.biography}"