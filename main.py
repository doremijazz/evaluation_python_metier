import email

from Business.goncourt import Goncourt
from daos.member_dao import MemberDao
from models.Book import Book
from models.Member import Member
from ihm.console import Console
from models.President import President


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
    goncourt.books = []
    goncourt.members = []
    goncourt.authors = []

    goncourt.init_db()

    goncourt.test_author_dao()

    goncourt.test_member_dao()

    goncourt.test_book_dao()


    while True:
        Console.principal_menu()
        choice = int(Console.choice_command())
        if choice == 1:
            email, pasword = Console.login_menu()
            status = goncourt.connection(email, pasword)
            print(f"status {status}")
            ##################################################
            if status == "President":
                while True:
                    Console.president_menu()
                    choice = int(Console.choice_command())
                    if choice == 1:
                        Book.display_all_books(goncourt.books)
                    elif choice == 2:
                        for member in goncourt.members:
                            member.display()
                    elif choice == 3:
                        if len(goncourt.books) > 8:
                            nb = 8;
                        elif len(goncourt.books) > 4:
                            nb = 4;
                        else:
                            nb = 1;
                        goncourt.books = President.enter_vote(goncourt.books)
                        print("Voici les livre selectionné, trié du plus choisi au moins choisi : ")
                        for i in range(nb):
                            print(goncourt.books[i])
                    elif choice == 4:
                        goncourt.books = President.announce_vote(goncourt.books)
                        print("\n\n-----------------------------------------------")
                        print("Voici les livre que vous avez selectionés : ")
                        for book in goncourt.books:
                            print(book)
                    elif choice == 0:
                        break
            #########################################################################
            elif status == "Member":
                while True:
                    Console.member_menu()
                    choice = int(Console.choice_command())
                    if choice == 1:
                        Book.display_all_books(goncourt.books)
                    elif choice == 2:
                        if len(goncourt.books) > 8:
                            nb = 8;
                        elif len(goncourt.books) > 4:
                            nb = 4;
                        else:
                            nb = 1;
                        books = Member.vote(goncourt.books, nb)
                        print(f"Les {nb} livre pour leqeuls vous avez voté")
                        Book.display_all_books(books)
                    elif choice == 0:
                        break
            ################################################
            elif status == "admin":
                while True:
                    Console.admin_menu()
                    choice = int(Console.choice_command())
                    if choice == 1:
                        member = Console.member_input()
                        goncourt.add_meber_to_db(member)
                    elif choice == 2:
                        member = Console.member_input()
                        goncourt.update_menber_in_db(member)
                    elif choice == 3:
                        name, surname = Console.member_to_delete()
                        member = goncourt.sursh_member(name, surname)
                        goncourt.delete_member_to_db(member)
                    elif choice == 4:
                        book = Console.book_input()
                        goncourt.add_book_to_db(book)
                    elif choice == 5:
                        book = Console.book_input()
                        goncourt.update_book_to_db(book)
                    elif choice == 6:
                        title = Console.book_to_delete()
                        book = goncourt.sursh_book(title)
                        goncourt.delete_book_to_db(book)




        elif choice == 2:
            Book.display_all_books(goncourt.books)
        elif choice == 0:
            break

if __name__ == "__main__":
    main()