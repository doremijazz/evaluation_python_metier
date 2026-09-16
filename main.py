from Business.goncourt import Goncourt
from models.Book import Book
from models.Member import Member
from ihm.console import Console


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

    goncourt.test_book_dao()

    while True:
        Console.principal_menu()
        choice : Console.choice_command()
        if choice == 1:
            pass
        elif choice == 2:
            Book.display_all_books(goncourt.books)
        elif choice == 0:
            break

if __name__ == "__main__":
    main()