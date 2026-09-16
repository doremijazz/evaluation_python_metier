from models.Member import Member


class Console:
    @staticmethod
    def principal_menu():
        print("########################\n")
        print("----- MENU PRINCIPAL ------")
        print("########################\n")
        print("1- Se connecter\n")
        print("2- Afficher tous les livres\n")
        print("0- Quitter\n")

    @staticmethod
    def president_menu():
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
        print("########################\n")
        print("----- MENU MEMBER ------")
        print("########################\n")
        print("1- Afficher tous les livres\n")
        print("2- Voter pour une selection de livre\n")
        print("0- Quitter\n")

    @staticmethod
    def message_display(message):
        print(message)

    @staticmethod
    def choice_command():
        return input("Votre choix : \n")

    @staticmethod
    def login_menu():
        print("#######################\n")
        print("----- MENU LOGIN ------")
        print("########################\n")
        email = input("Entrez votre email : \n")
        password = input("Entrez votre password : \n")
        return email,password

    @staticmethod
    def member_input()-> Member:
        name = input("Entrez le prénom : ")
        surname = input("Entrez le nom de famille : \n")
        age = input("Entrez l'age : \n")
        email = input("Entrez l'email : \n")
        password = input("Entrez le mot de passe initial : ")
        status = input("Quel est dont status (president ou membre ou admin) ? : \n")
        member = Member(name,surname,age,email,password,status)
        return member


