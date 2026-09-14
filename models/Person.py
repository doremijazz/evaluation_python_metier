# -*- coding: utf-8 -*-

"""
Classe abstraite Person, mère de Student et Teacher
"""
from abc import ABC
from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class Person(ABC):
    """Person liée au concours : président ou membre ou auteur"""
    first_name: ClassVar[str] = field(init=False)
    last_name: ClassVar[str] = field(init=False)
    age: ClassVar[int] = field(init=False)

    def display(self):
        pass