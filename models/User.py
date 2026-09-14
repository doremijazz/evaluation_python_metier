from dataclasses import dataclass, field
from typing import ClassVar

from models.Person import Person


@dataclass
class User(Person):
    user_id: ClassVar[int] = 0
    user_nbr: int = field(init=False)
    email: ClassVar[str] = field(init=False)
    password: ClassVar[str] = field(init=False)
    statut : ClassVar[str] = field(init=False)

    def display(self):
        print(self.user_id)
        print(self.email)
        print(self.password)
        print(self.statut)

    def connect(self):
        pass
