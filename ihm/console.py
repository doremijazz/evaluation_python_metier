from datetime import date

from pymysql.constants.FIELD_TYPE import NULL

from models.Author import Author
from models.Book import Book
from models.Member import Member


class Console:
    """Regrouper l'affichage des menus et la collecte des saisies utilisateur."""

    @staticmethod
    def principal_menu():
        """Afficher les choix du menu principal."""

        print("########################\n")
        print("----- MENU PRINCIPAL ------")
        print("########################\n")
        print("1- Se connecter\n")
        print("2- Afficher tous les livres\n")
        print("0- Quitter\n")

    @staticmethod
    def president_menu():
        """Afficher les actions accessibles au président."""

        print("##########################\n")
        print("----- MENU PRESIDENT ------")
        print("#########################\n")
        print("1- Afficher tous les livres\n")
        print("2- Afficher tous les membres\n")
        print("3- Saisir les votes\n")
        print("4- Saisir la selection de livre pour le prochian tour\n")
        print("0- Quitter\n")

    @staticmethod
    def admin_menu():
        """Afficher les actions de gestion accessibles à l'administrateur."""

        print("#########################\n")
        print("----- MENU ADMIN ------")
        print("#########################\n")
        print("1- Ajouter un membre\n")
        print("2- Modifier un membres\n")
        print("3- Suprimer un membre\n")
        print("4- Ajouter un livre\n")
        print("5- Modifier un livre\n")
        print("6- Suprimer un livre\n")
        print("0- Quitter\n")

    @staticmethod
    def member_menu():
        """Afficher les actions accessibles à un membre du jury."""

        print("########################\n")
        print("----- MENU MEMBER ------")
        print("########################\n")
        print("1- Afficher tous les livres\n")
        print("2- Voter pour une selection de livre\n")
        print("0- Quitter\n")

    @staticmethod
    def message_display(message):
        """Afficher un message transmis par une autre couche."""

        print(message)

    @staticmethod
    def choice_command():
        """Lire et retourner un choix de menu sous forme de texte."""

        return input("Votre choix : \n")

    @staticmethod
    def login_menu():
        """Demander les identifiants et les retourner sous forme de tuple."""

        print("#######################\n")
        print("----- MENU LOGIN ------")
        print("########################\n")
        email = input("Entrez votre email : \n")
        password = input("Entrez votre password : \n")
        return email,password

    @staticmethod
    def member_input()-> Member:
        """Construire un membre à partir des informations saisies."""

        name = input("Entrez le prénom : ")
        surname = input("Entrez le nom de famille : \n")
        age = int(input("Entrez l'age : \n"))
        email = input("Entrez l'email : \n")
        password = input("Entrez le mot de passe initial : ")
        status = input("Quel est dont status (president ou membre ou admin) ? : \n")
        member = Member(name,surname,age,email,password,status)
        return member

    @staticmethod
    def member_to_delete():
        """Demander l'identité du membre à supprimer."""

        name = input("Entrez le prénom du membre : ")
        surname = input("Entrez le nom de famille : ")
        return name,surname

    def book_input(self):
        """Construire un livre et son auteur à partir des saisies console."""

        title = input("Entrez le nom du livre : ")
        author_name = input("Entrez le prénom de l'auteur : \n : ")
        author_surname = input("Entrez le nom de famille de l'auteur : \n")
        author : Author = Author(author_name,author_surname,NULL," ")
        resum =input("Entrez un resumé du livre : ")
        publish_days = input("Entrez le jour de la date d'édition du livre : ")
        publish_month = input("Enter le numéro du mois de la date d'édition : \n")
        publish_year = input("Entrer l'année d'édition : \n")
        publish_date = date(int(publish_year),int(publish_month),int(publish_days))
        editeur = input("Entrez le nom de l'editeur : \n ")
        pp = input("Entrez les personnage principaux : ")
        nb_pages = input("Entrez le nom de le nombre de pages : \n")
        isbn = input("Entrez le nom de l'ISBN : \n")
        price = float(input("Entrez le nom du livre : "))
        book : Book = Book(title,author, resum, publish_date, editeur,pp,nb_pages,isbn,price)
        return book

    def book_to_delete(self):
        """Demander le titre du livre à supprimer."""

        title = input("Entrez le nom du livre : ")
        return title