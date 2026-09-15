from dataclasses import dataclass, field
from typing import ClassVar

from models.Person import Person


@dataclass
class User(Person):
    user_id: ClassVar[int] = 0
    user_nbr: int = field(init=False)
    email: str
    password: str
    statut : str

    def __post_init__(self):
        User.user_id += 1
        self.user_nbr = User.user_id

    def display(self):
        person_str = super().__str__()
        print(f"Utilisateur : {person_str}.")
        print(f" ID : {self.user_id}, \n"
              f" email :{self.email}, \n"
              f" password :{self.password}, \n"
              f" status :{self.statut}")

    def connect(self):
        pass

    def __str__(self):
        person_str = super().__str__()
        return f"{person_str}. \nemail :{self.email}, \nstatut : {self.statut}"
