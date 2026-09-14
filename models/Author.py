from dataclasses import dataclass

from models.Person import Person


@dataclass
class Author(Person):
    biography: str

    def display(self):
        person_str = super().__str__()
        print(f"{person_str}. \n Biographie : {self.biography}")