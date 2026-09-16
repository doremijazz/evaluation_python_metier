from Business.goncourt import Goncourt
from models.Book import Book
from models.Member import Member


def main() -> None:
    goncourt : Goncourt = Goncourt()
    print("Goncourt")
    print("-------------------------\n"
          "TEST EN STATIC\n"
          "-------------------------\n\n")

    goncourt.init_static()
    print("########################\n"
          "Affichage en static de tous les livres\n")
    Book.display_all_books(goncourt.books)

    print("########################\n"
          "Affichage en static de tous les auteurs\n")
    for author in goncourt.authors:
        author.display()

    print("########################\n"
          "Affichage en static de tous les membre\n")
    for member in goncourt.members:
        member.display()

    print("-------------------------\n"
          "TEST EN BDD\n"
          "-------------------------\n\n")

    goncourt.test_author_dao()

    goncourt.test_member_dao()

if __name__ == "__main__":
    main()