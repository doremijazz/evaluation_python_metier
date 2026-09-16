from dataclasses import dataclass, field
from typing import ClassVar

from models.Person import Person


@dataclass
class Author(Person):
    author_id: ClassVar[int] = 0
    author_nbr: int = field(init=False)
    biography: str

    def __post_init__(self):
        Author.author_id +=1
        Author.author_nbr = self.author_id

    def display(self):
        person_str = super().__str__()
        print(f"{person_str}. \n Biographie : {self.biography}")

    def __str__(self):
        person_str = super().__str__()
        return f"{person_str}. \n Biographie : {self.biography}"