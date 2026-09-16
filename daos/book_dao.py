from dataclasses import dataclass
from typing import Optional

from daos.author_dao import AuthorDao
from daos.dao import Dao
from models.Author import Author
from models.Book import Book
from models.Person import Person


@dataclass
class BookDao(Dao[Book]):
    def create(self, book: Book) -> int:
        id_book = Optional[int]
        try:
            with Dao.connection.cursor() as cursor:
                print("avant sql")
                sql = "INSERT INTO pg_livre (l_ID_auteur, l_title, l_editeur, l_publish_date, l_resume, l_pp, l_nb_pages, l_isbn, l_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                pp : str = book.pp[0]
                i = 1
                print("entre deux")
                sql_id_author = "SELECT DISTINCT A.aut_ID_auteur FROM pg_auteur A INNER JOIN pg_person P ON A.p_ID_person = P.p_ID_person WHERE P.p_name = %s AND P.p_surname = %s"
                print(f"nom du livre : {book.title}")
                print(f"nom de l'auteur {book.author.first_name}")
                cursor.execute(sql_id_author, (book.author.first_name, book.author.last_name))
                record = cursor.fetchone()
                print(f"record : {record}")
                if record is not None:
                    id_author = record['aut_ID_auteur']

                else :
                    author_dao : AuthorDao = AuthorDao()
                    id_author = author_dao.create(book.author)
                while i < len(book.pp):
                    pp = pp + "," + book.pp[i]
                    i+=1

                print(f"author nbr : {book.author.author_id}")
                print(f"id_author : {id_author}")

                print(f"personage principaux : {pp}")
                cursor.execute(sql, (id_author, book.title, book.editeur, book.publish_date, book.resume, pp, book.nb_pages, book.isbn, book.price))
                print("apres sql")
                id_book = cursor.lastrowid
                Book.id = id_book
                Book.book_nbr = id_book

                Dao.connection.commit()
                return id_book
        except Exception as e:
            print(f"Erreur lors de la création du livre : {e}")
            Dao.connection.rollback()
            return 0

    def book_from_db(self, record)-> Book:
        book : Book = Book( record["l_title"], record['l_ID_auteur'], record["l_resume"], record['l_publish_date'], record["l_editeur"], record["l_pp"], record["l_nb_pages"], record["l_isbn"], record["l_price"])
        book.id = record["l_ID_livre"]
        return book

    def read(self, book_id: int) -> Book:
        book : Optional[Book]
        try:
            with Dao.connection.cursor() as cursor:
                sql = "SELECT * FROM pg_livre WHERE l_ID_livre = %s"
                cursor.execute(sql, (book_id,))
                record = cursor.fetchone()
                if record is not None:
                    book = self.book_from_db(record)
                    author_dao : AuthorDao = AuthorDao()
                    book.author = author_dao.read(book.author)
                    print(f"book author : {book.author}")
                else:
                    book = None
                return book
        except Exception as e:
            print(f"Erreur lors de la lecture du livre : {e}")


    def readAll(self) -> list[Book]:
        book_list : list[Book] = []
        try:
            with Dao.connection.cursor() as cursor:
                sql = "SELECT * FROM pg_livre ORDER BY l_ID_livre"
                cursor.execute(sql)
                records = cursor.fetchall()
                for record in records:
                    book = self.book_from_db(record)
                    author_dao: AuthorDao = AuthorDao()
                    book.author = author_dao.read(book.author)
                    book_list.append(book)
                return book_list
        except Exception as e:
            print(f"Erreur lors de la lecture de tous les livres : {e}")




    def update(self, book: Book) -> bool:
        try:
            with Dao.connection.cursor() as cursor:
                sql = "UPDATE pg_livre SET l_ID_auteur=%, l_title=%,l_editeur=%s, l_resume=%s, l_pp=%s, l_nb_pages=%s, l_isbn=%s, l_price=%s WHERE l_ID_livre=%s"
                cursor.execute(sql, (book.author.author_nbr, book.title, book.editeur, book.resume, book.pp, book.nb_pages, book.isbn,book.price, book.id))
                Dao.connection.commit()
                return True
        except Exception as e:
            print(f"Erreur lors de la modification du livre : {e}")
            Dao.connection.rollback()
            return False



    def delete(self, book: Book) -> bool:
        try:
            with Dao.connection.cursor() as cursor:
                sql = "DELETE FROM pg_livre WHERE l_ID_livre = %s"
                print(f"book_id : {book.book_nbr}")
                cursor.execute(sql, (book.book_nbr,))
                Dao.connection.commit()
                return True
        except Exception as e:
            print(f"Erreur lors de la supression du livre : {e}")
            return False

    def sursh(self, title: str) -> Optional[Book]:
        try:
            with Dao.connection.cursor() as cursor:
                sql = "SELECT * FROM pg_livre WHERE l_title = %s"
                cursor.execute(sql, (title,))
                record = cursor.fetchone()
                if record is not None:
                    book = self.book_from_db(record)
                else:
                    book = None
        except Exception as e:
            print(f"Erreur lors de la recherche du livre : {e}")