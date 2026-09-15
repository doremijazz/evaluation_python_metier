from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import ClassVar, Optional

import pymysql


@dataclass
class Dao[T](ABC):
    connection: ClassVar[pymysql.Connection] = \
        pymysql.connect(host='localhost',
                        user='abinet002',
                        database='prix_goncourt',
                        cursorclass=pymysql.cursors.DictCursor)
    @abstractmethod
    def create(self, obj: T) ->int :
        """Crée l'entité en BD correspondant à l'objet obj

               :param obj: à créer sous forme d'entité en BD
               :return: l'id de l'entité insérée en BD (0 si la création a échoué)
               """
        ...

    @abstractmethod
    def read(self, id_entity : int) -> Optional[T]:
        """Renvoit l'objet correspondant à l'entité dont l'id est id_entity
                  (ou None s'il n'a pu être trouvé)"""
        ...


    @abstractmethod
    def readAll(self) -> list[T]:
        """Renvoit l'ensemble des entités de la BD correspondant à la classe de modèle T."""
        ...

    @abstractmethod
    def update(self, obj : T) -> bool:
        """Met à jour en BD l'entité correspondant à obj, pour y correspondre

                :param obj: objet déjà mis à jour en mémoire
                :return: True si la mise à jour a pu être réalisée
                """
        ...

    def delete(self, obj : T) -> bool:
        """Supprime en BD l'entité correspondant à obj

               :param obj: objet dont l'entité correspondante est à supprimer
               :return: True si la suppression a pu être réalisée
               """
        ...