# -*- coding: utf-8 -*-

"""
Classe abstraite Person, mère de Student et Teacher
"""
from abc import ABC
from dataclasses import dataclass, field

@dataclass
class Person(ABC):
    """Person liée au concours : président ou membre ou auteur"""
    first_name: str
    last_name: str
    age: int

    def display(self):
        pass