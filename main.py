from Business.goncourt import Goncourt
from models.Book import Book


def main() -> None:
    goncourt : Goncourt = Goncourt()

    goncourt.init_static()
    Book.display_all_books(goncourt.books)
    for author in goncourt.authors:
        author.display()
    for member in goncourt.members:
        member.display()

    goncourt.test_author_dao()

if __name__ == "__main__":
    main()