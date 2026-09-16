from dataclasses import dataclass
from typing import Optional

from daos.dao import Dao
from models.Author import Author
from models.Book import Book


@dataclass
class BookDao(Dao[Book]):
    def create(self, book: Book) -> int:
        id_book = Optional[int]
        try:
            with Dao.connection.cursor() as cursor:
                sql = "INSERT INTO books (l_ID_auteur, l_title,l_editeur, l_resume, l_pp, l_nb_pages, l_isbn, l_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (book.author.author_nbr, book.title, book.editeur, book.resume, book.pp, book.nb_pages, book.isbn,book.price))
                id_book = cursor.lastrowid
                Book.id = id_book
                Book.book_nbr = id_book

                Dao.connection.commit()
                return id_book
        except Exception as e:
            print(f"Erreur lors de la création du livre : {e}")
            Dao.connection.rollback()
            return 0


    def read(self, book_id: int) -> Book:
        pass
    def readAll(self) -> list[Book]:
        pass
    def update(self, book: Book) -> bool:
        pass
    def delete(self, book: Book) -> bool:
        pass