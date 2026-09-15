from typing import Optional

from daos.dao import Dao
from models.Author import Author


class AuthorDao(Dao[Author]):
    def create(self, author : Author) -> int:
        id_author : Optional[int]=None
        id_person : int
        try:
            with Dao.connection.cursor() as cursor:
                sql_person ="INSERT INTO person (p_surname, p_name, p_age) VALUES (%s, %s, %s)"
                cursor.execute(sql_person, (author.last_name, author.first_name, author.age))
                id_person = cursor.lastrowid

                sql_author ="INSERT INTO author (aut_bio, p_ID_person) VALUES (%s, %s, %s)"
                cursor.execute(sql_author,(author.biography, id_person))
                id_author = cursor.lastrowid

                Dao.connection.commit()
                return id_author
        except Exception as e :
            print(f"Erreur lors de la création de l'auteur : {e}")
            Dao.connection.rollback()
            return 0

    def author_from_db(record)->Author:
        author: Author = Author(record['p_surname'], record['p_name'], record['p_age'], record["aut_bio"])
        return author

    def read(self, id_author: int) -> Author:
            author : Optional[Author]

            try:
                with Dao.connection.cursor() as cursor:
                    sql = "SELECT * FROM pg_author A INNER JOIN pg_person P on A.p_ID_person = P.p_ID_person WHERE id_author = %s"
                    cursor.execute(sql, (id_author,))
                    record = cursor.fetchone()
                    if record is not None:
                        author = self.author_from_db(record)
                    else :
                        author = None

                    return author
            except Exception as e :
                print(f"Erreur lors de la lecture de l'auteur: {e}")

    def readAll(self) -> list[Author]:
        author_list:list[Author] = []
        try :
            with Dao.connection.cursor() as cursor:
                sql = "SELECT * FROM pg_author A INNER JOIN pg_person P on A.p_ID_person = P.p_ID_person"
                cursor.execute(sql)
                records = cursor.fetchall()
                for record in records:
                    author_list.append(self.author_from_db(record))
                return author_list
        except Exception as e :
            print(f"Erreur lors de la lecture de tous les auteurs : {e}")

    def update(self, author : Author) -> bool:
        try :
            with Dao.connection.cursor() as cursor:
                sql_person ="UPDATE pg_person P JOIN pg_author A ON A.p_ID_person = P.p_ID_person SET P.p_surname = %s, P.p_name = %s, P.p_age = %s, A.aut_bio = % WHERE A.aut_ID_auteur = %s"
                cursor.execute(sql_person, (author.last_name, author.first_name, author.age, author.biography))
                Dao.connection.commit()
                return True
        except Exception as e :
            print(f"Erreur lors de la modification de l'auteur : {e}")
            Dao.connection.rollback()
            return False


    def delete(self, author : Author) -> bool:
        try :
            with Dao.connection.cursor() as cursor:
                sql_slect_person = "SELECT P.p_ID_person FORM pg_person INNER JOIN pg_auteur P on P.p_ID_person = A.p_ID_person WHERE A.aut_ID_auteur = %s"
                cursor.execute(sql_slect_person,(author.author_nbr,))
                record = cursor.fetchone()
                id_person = int = record["id_person"]

                sql_author = "DELETE FROM pg_author  WHERE A.aut_ID_auteur = %s"
                cursor.execute(sql_author,(author.author_nbr,))

                sql_person = "DELETE FROM pg_person  WHERE P.p_ID_person = %s"
                cursor.execute(sql_person,(id_person,))

                Dao.connection.commit()
                return True
        except Exception as e :
            print(f"Erreur lors de la suppression de l'auteur : {e}")
            Dao.connection.rollback()
            return False
        

        ...
