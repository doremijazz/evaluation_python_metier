# -*- coding: utf-8 -*-

"""
Classe goncourt
"""
import os
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Optional

from daos import author_dao, book_dao
from daos.author_dao import AuthorDao
from daos.book_dao import BookDao
from daos.connection_dao import ConnectionDao
from daos.member_dao import MemberDao
from daos.dao import Dao
from models.Person import Person
from models.President import President
from models.User import User
from models.Author import Author
from models.Book import Book
from models.Member import Member


@dataclass
class Goncourt:
    """Couche metier de l'application de gestion du concours goncourt
    reprenant les cas d'utilisation et les spécifications fonctionnelles
    -book : liste des 16 livres prés selctioné
    -author : liste des auteurs
    -member : liste des membres
    -president : le president
    -user : liste des utilisateurs
    """
    books: list[Book] = field(default_factory=list, init=False)
    authors: list[Author] = field(default_factory=list, init=False)
    members: list[Member] = field(default_factory=list, init=False)

    def add_book(self,book:Book):
        self.books.append(book)

    def add_book_to_db(self,book:Book)->bool:
        try:
            book_dao : BookDao = BookDao()
            book_dao.create(book)
            return True
        except Exception as e:
            print(f"Erreur lors de la creation de book en bd : {e}")
            return False

    def sursh_book_in_db(self, title :str)-> Optional[Book]:
        try :
            book_dao : BookDao = BookDao()
            book : Book = book_dao.sursh(title)
            return book
        except Exception as e:
            print(f"Erreur dans la recherche du livre en db : {e}")
            return None


    def update_book_to_db(self,book:Book)->bool:
        try:
            book_dao : BookDao = BookDao()
            book_dao.update(book)
            return True
        except Exception as e:
            print(f"Erreur lors de MAJ du livre en db : {e}")
            return False

    def add_author(self,author:Author):
        self.authors.append(author)

    def add_member(self,member:Member):
        self.members.append(member)

    @staticmethod
    def add_meber_to_db (menber : Member) -> bool:
        try :
            menber_dao : MemberDao = MemberDao()
            menber_dao.create(menber)
            return True
        except Exception as e:
            print(f"Erreur lors de lajout a la db du memnbre : {e}")
            return False

    @staticmethod
    def update_member_in_db(member : Member)-> bool:
        try:
            member_dao : MemberDao = MemberDao()
            member_dao.update(member)
            return True
        except Exception as e:
            print(f"Erreur lors de MAJ du membre en db : {e}")
            return False

    @staticmethod
    def delete_member_to_db (member : Member) -> bool:
        try:
            member_dao : MemberDao = MemberDao()
            member_dao.delete(member)
            return True
        except Exception as e:
            print(f"Erreur lors de la supression du membre en db : {e}")

    @staticmethod
    def sursh_member(name, surname)-> Optional[Member]:
        try :
            member_dao : MemberDao = MemberDao()
            member = member_dao.sursh(name, surname)
            return member
        except Exception as e:
            print(f"Erreur lors de la recherche du membre : {e}")


    def get_author(author_nbr : int)->Optional[Author]:
        author_dao : AuthorDao = AuthorDao()
        return author_dao.read(author_nbr)

    def initialize_person_counter(self) -> None:
        with Dao.connection.cursor() as cursor:
            sql = """
                SELECT COALESCE(MAX(p_ID_person), 0) AS max_id_person
                FROM pg_person
            """

            cursor.execute(sql)
            record = cursor.fetchone()

        Person.id_person = (record["max_id_person"]-1)

    def initialize_author_counter(self) -> None:
        with Dao.connection.cursor() as cursor:
            sql = """
                SELECT COALESCE(MAX(aut_ID_auteur), 0) AS max_id_auteur
                FROM pg_auteur
            """

            cursor.execute(sql)
            record = cursor.fetchone()

        Author.author_id = record["max_id_auteur"]


    def test_author_dao(self) -> None:

        print("_______________________________________ \n"
        "TEST AUTEUR DAO\n"
        "_______________________________________ \n\n")
        author_dao : AuthorDao = AuthorDao()

        moi : Author = Author("anais", "binet", 26, "blablabla")
        self.add_author(moi)
        id = author_dao.create(moi)
        print (f"* Ajout d'un auteur dont l'id est {id} \n")
        #print(moi)
        os.system('pause')

        print("###############################################\n"
              "Lecture de auteur dans la base de données -> \n")
        auteur =author_dao.read(id)
        auteur.display()
        os.system('pause')
        print("###############################################\n"
              "Lecture de tous les auteurs de la base de données \n")
        les_auteur = author_dao.readAll()
        for un_auteur in les_auteur:
            un_auteur.display()

        #print("a", a)
        moi.author_id = auteur.author_id

        os.system('pause')
        sucess = author_dao.delete(moi)
        print("###############################################"
              f"Supression du auteur de la base de données reussi ? -> {sucess}")
        Author.author_id -=1

    def test_member_dao(self) -> None:
        print("_______________________________________ \n"
                "TEST MEMBRE DAO\n"
                "_______________________________________ \n\n")
        member_dao : MemberDao = MemberDao()

        victor : Member = Member("victor", "sueur", 25, "victorsueur30@gmail.com", "1234", "Member")

        self.add_member(victor)
        id = member_dao.create(victor)
        print(f"* Ajout d'un membre dont l'id est {id} \n")
        os.system('pause')
        print("###############################################\n"
              "Lecture de membre dans la base de données -> \n")
        membre = member_dao.read(id)
        membre.display()
        os.system('pause')
        print("###############################################\n"
              "Lecture de tous les membres de la base de données \n")

        les_membre =member_dao.readAll()
        for membre in les_membre:
            membre.display()

        sucess = member_dao.delete(victor)
        os.system('pause')
        print("###############################################\n"
              f"Supression du membre de la base de données reussi ? -> {sucess}")
        Member.member_id -= 1

    def test_book_dao(self)->None:
        print("_______________________________________ \n"
              "TEST BOOK DAO\n"
              "_______________________________________ \n\n")
        book_dao : BookDao = BookDao()
        livre : Book = Book(
            "Livre de test",
            Author(
                "Christine",
                "Pertus",
                53,
                "Christine Pertus Binet est une formatrice française née en 1973. "
            ),
            "A la MFR de lesparre medoc elle est directrice adjointe et référente handicap",
            date(2026, 9, 16),
            "Larousse",
            ["l'autrice", "les élèves de la MFR"],
            96,
            "1111111111",
            6.5
        )
        self.add_book(livre)
        id = book_dao.create(livre)
        print(f"* Ajout d'un book dont l'id est {id} \n")
        os.system('pause')
        print("###############################################\n"
              "Lecture d'un livre dans la base de données -> \n")
        book = book_dao.read(id)
        print(book)
        os.system('pause')
        print("###############################################\n"
              "Lecture de tous les membres de la base de données \n")
        books = book_dao.readAll()
        for book in books:
            print(book)
        os.system('pause')
        sucess = book_dao.delete(livre)
        print("###############################################\n"
              f"Supression du livre dans la base de données reussi ? -> {sucess}")



    def init_static(self):
        """Initialisation du static de l'application de gestion"""
        president = President("Dedier", "DECOIN", 81, "dedier@gncourt.fr", "1234", "President")
        francoise : Member = Member("Francoise", "Chandernagor", 81, "francoise@goncourt.fr", "1234", "Member")
        tahar : Member = Member("Tahar Ben", "Jelloun", 81, "taharben@goncourt.fr", "1234", "Member")
        paul : Member = Member("Paul", "Constant", 82, "paul@goncourt.fr", "1234", "Member")
        philippe : Member = Member("Philippe", "Claudel", 64, "philippe@goncourt.fr","1234", "Member")
        pierre : Member = Member("Pierre", "Assouline", 73, "pierre@goncourt.fr", "1234", "Member")
        eric : Member = Member("Eric-Emannuel", "Schmitt", 66, "eric@goncourt.fr", "1234", "Member")
        camille : Member = Member("Camille", "Laurens", 68, "camille@goncourt.fr", "1234", "Member")
        pascal : Member = Member("Pascal", "Bruckner", 77, "pascal@goncourt.fr", "1234", "Member")
        christine : Member = Member("Christine", "Angot", 67, "christine@goncourt.fr", "1234", "Member")

        for member in [francoise,tahar,paul,philippe,pierre,eric,camille,pascal,christine]:
            self.members.append(member)


        minotaure: Book = Book(
            "Minotaure",
            Author(
                "Boris",
                "Bergmann",
                34,
                "Boris Bergmann est un écrivain français né en 1992 à Paris. "
                "Il publie son premier roman à l'adolescence et développe une œuvre "
                "consacrée à la jeunesse, à l'identité et à la société contemporaine."
            ),
            "À 23 ans, un jeune homme part à la rencontre de son père, qu'il n'a jamais "
            "connu, dans son cabinet de psychiatre. Ce récit autobiographique raconte "
            "sa quête familiale et rend hommage à sa mère.",
            date(2026, 8, 19),
            "Albin Michel",
            ["le narrateur", "son père", "sa mère"],
            256,
            "2226511873",
            20.90
        )
        self.add_author(minotaure.author)
        self.add_book(minotaure)

        faire_la_peau: Book = Book(
            "Faire la peau",
            Author(
                "Louise",
                "Chennevière",
                39,
                "Louise Chennevière est une écrivaine française. Elle est notamment "
                "l'autrice de Comme la chienne, Mausolée et Pour Britney. Son œuvre "
                "interroge la condition féminine, la violence sociale et les relations familiales."
            ),
            "À trente ans, une femme tente de se libérer de l'emprise de sa mère et "
            "d'une lignée familiale marquée par la violence. Elle revisite son enfance "
            "et son adolescence afin de comprendre ce lien mêlant colère, amour et dépendance.",
            date(2026, 8, 20),
            "P.O.L",
            ["la narratrice", "sa mère"],
            288,
            "2818063583",
            21.00
        )
        self.add_book(faire_la_peau)
        self.add_author(faire_la_peau.author)

        chronique_royaume_perdu: Book = Book(
            "Chronique d'un royaume perdu",
            Author(
                "Ananda",
                "Devi",
                69,
                "Ananda Devi est une écrivaine mauricienne francophone née en 1957. "
                "Romancière, nouvelliste et poétesse, elle construit une œuvre consacrée "
                "à l'identité, à la violence, à l'exclusion et à la société mauricienne."
            ),
            "Au Bouchon, un village isolé de l'île Maurice, quatre générations se "
            "succèdent depuis l'époque de l'esclavage. Un enfant devient le chroniqueur "
            "de ce royaume afin d'en conserver les luttes, les amours et la mémoire.",
            date(2026, 8, 19),
            "Grasset",
            ["le chroniqueur", "les habitants du Bouchon"],
            464,
            "2246846943",
            24.00
        )
        self.add_book(chronique_royaume_perdu)
        self.add_author(chronique_royaume_perdu.author)
        le_fabuleux_piano: Book = Book(
            "Le fabuleux piano",
            Author(
                "Sonia",
                "Devillers",
                51,
                "Sonia Devillers est une journaliste, animatrice de radio et écrivaine "
                "française née en 1975. Dans ses livres, elle explore notamment la mémoire "
                "familiale, l'exil et l'histoire des Juifs de Roumanie."
            ),
            "Sonia Devillers recherche un piano à queue volé à une famille juive par "
            "les nazis en 1943. Son enquête sur les instruments pillés pendant "
            "l'Occupation fait résonner l'histoire collective avec celle de sa propre grand-mère.",
            date(2026, 8, 27),
            "Robert Laffont",
            ["la narratrice", "sa grand-mère", "les propriétaires du piano"],
            288,
            "2221286804",
            21.00
        )
        self.add_book(le_fabuleux_piano)
        self.add_author(le_fabuleux_piano.author)
        nous_aussi: Book = Book(
            "Nous aussi",
            Author(
                "Anne",
                "Godard",
                55,
                "Anne Godard est une écrivaine française. Son travail littéraire explore "
                "l'intimité, les relations familiales, le corps et les bouleversements "
                "qui traversent l'existence quotidienne."
            ),
            "Un récit consacré à des personnages confrontés à leur histoire intime et "
            "familiale. Le roman examine ce qui rapproche les êtres, mais également "
            "les silences et les blessures qui les séparent.",
            date(2026, 8, 19),
            "Actes Sud",
            ["la narratrice", "sa famille"],
            192,
            "2330225571",
            20.00
        )
        self.add_book(nous_aussi)
        self.add_author(nous_aussi.author)

        joseph_dans_la_nuit: Book = Book(
            "Joseph dans la nuit",
            Author(
                "Olivier",
                "Grondeau",
                49,
                "Olivier Grondeau est un écrivain français. Arrêté en Iran en 2022, "
                "il a été détenu pendant plus de deux ans avant de revenir en France. "
                "Son écriture témoigne de l'enfermement, de la solitude et de la résistance."
            ),
            "À travers le personnage de Joseph, le récit évoque l'enfermement, la nuit "
            "carcérale et les pensées qui permettent de résister. Le protagoniste tente "
            "de préserver son identité malgré l'isolement et l'incertitude.",
            date(2026, 8, 20),
            "L'Iconoclaste",
            ["Joseph", "ses proches", "ses gardiens"],
            224,
            "237880492X",
            19.90
        )
        self.add_book(joseph_dans_la_nuit)
        self.add_author(joseph_dans_la_nuit.author)

        solitude_professeurs: Book = Book(
            "La solitude des professeurs est infinie",
            Author(
                "Yannick",
                "Haenel",
                59,
                "Yannick Haenel est un écrivain français né en 1967. Ancien professeur "
                "de français, il est notamment l'auteur de Cercle, Jan Karski et "
                "Tiens ferme ta couronne."
            ),
            "Un professeur observe la transformation de son métier et la manière dont "
            "l'école est considérée par la société. Le roman aborde la transmission, "
            "la vocation d'enseigner et la solitude ressentie face aux difficultés "
            "du système scolaire.",
            date(2026, 8, 20),
            "Gallimard",
            ["le professeur", "ses élèves", "ses collègues"],
            320,
            "2073101542",
            21.50
        )
        self.add_book(solitude_professeurs)
        self.add_author(solitude_professeurs.author)

        je: Book = Book(
            "Je",
            Author(
                "Lilia",
                "Hassaine",
                35,
                "Lilia Hassaine est une journaliste et romancière française née en 1991. "
                "Elle est notamment l'autrice de L'Œil du paon, Soleil amer et Panorama. "
                "Ses romans examinent l'identité, les apparences et les transformations sociales."
            ),
            "Le roman redonne une voix à une femme jusque-là enfermée dans le regard "
            "et le récit des autres. Elle raconte son existence à la première personne "
            "et tente de reprendre possession de son identité.",
            date(2026, 8, 20),
            "Gallimard",
            ["la narratrice"],
            256,
            "2073099947",
            20.50
        )
        self.add_book(je)
        self.add_author(je.author)

        inconnue_quai_javel: Book = Book(
            "L'inconnue du quai de Javel",
            Author(
                "Philippe",
                "Jaenada",
                62,
                "Philippe Jaenada est un écrivain français né en 1964. Il est connu pour "
                "ses enquêtes littéraires dans lesquelles il revient sur des affaires "
                "criminelles et tente de restituer la vie de personnes oubliées."
            ),
            "Philippe Jaenada enquête sur une jeune femme retrouvée morte près du quai "
            "de Javel. À partir des archives disponibles, il cherche à reconstruire son "
            "identité, son parcours et les circonstances de sa disparition.",
            date(2026, 8, 19),
            "Flammarion",
            ["la jeune inconnue", "le narrateur", "les enquêteurs"],
            528,
            "2080490893",
            24.00
        )
        self.add_book(inconnue_quai_javel)
        self.add_author(inconnue_quai_javel.author)

        une_foret: Book = Book(
            "Une forêt",
            Author(
                "Jean-Yves",
                "Jouannais",
                62,
                "Jean-Yves Jouannais est un écrivain, critique d'art et commissaire "
                "d'exposition français né en 1964. Ses travaux associent littérature, "
                "histoire de l'art, mémoire et réflexion sur la guerre."
            ),
            "Le narrateur traverse une forêt réelle et mentale dans laquelle les "
            "souvenirs, les œuvres et les événements historiques se répondent. "
            "Le paysage devient progressivement un espace de mémoire et de réflexion.",
            date(2026, 8, 19),
            "Albin Michel",
            ["le narrateur"],
            112,
            "2226499520",
            17.90
        )
        self.add_book(une_foret)
        self.add_author(une_foret.author)

        nefface_pas_mes_cercles: Book = Book(
            "N'efface pas mes cercles",
            Author(
                "Emma",
                "Marsantes",
                39,
                "Emma Marsantes est une écrivaine française. Ses romans explorent les "
                "secrets familiaux, les traumatismes transmis entre les générations "
                "et la manière dont les individus reconstruisent leur histoire."
            ),
            "En 1980, une femme se suicide dans un appartement. Le roman remonte le "
            "temps pour comprendre son histoire, son mariage dans les années 1950 "
            "et les destins brisés qui ont marqué plusieurs générations.",
            date(2026, 8, 20),
            "Verdier",
            ["la femme", "son mari", "leur famille"],
            160,
            "2378562950",
            19.50
        )
        self.add_book(nefface_pas_mes_cercles)
        self.add_author(nefface_pas_mes_cercles.author)

        choses_perdues: Book = Book(
            "Choses que je croyais perdues",
            Author(
                "Clémentine",
                "Mélois",
                46,
                "Clémentine Mélois est une artiste plasticienne, photographe et écrivaine "
                "française née en 1980. Membre de l'Oulipo, elle associe dans son travail "
                "la littérature, l'image, l'humour et les objets du quotidien."
            ),
            "Alors qu'Émilie prépare son déménagement, les objets qu'elle retrouve "
            "font réapparaître des souvenirs qu'elle pensait disparus. Chaque chose "
            "devient le point de départ d'une évocation intime, drôle ou mélancolique.",
            date(2026, 8, 20),
            "L'Arbalète/Gallimard",
            ["Émilie", "ses proches"],
            176,
            "2073112641",
            19.50
        )
        self.add_book(choses_perdues)
        self.add_author(choses_perdues.author)

        cetait_ca_ou_mourir: Book = Book(
            "C'était ça ou mourir",
            Author(
                "Thélyson",
                "Orélien",
                38,
                "Thélyson Orélien est un poète, romancier et critique haïtien. "
                "Son œuvre est traversée par la mémoire, l'exil, la violence politique "
                "et la recherche d'une appartenance."
            ),
            "Après l'embrasement de son quartier de Port-au-Prince, Jonas Dorléon quitte "
            "Haïti avec un diplôme, un cahier de poèmes et une photographie de sa mère. "
            "Le roman raconte son exil et sa lutte pour reconstruire sa vie.",
            date(2026, 8, 19),
            "Grasset",
            ["Jonas Dorléon", "sa mère"],
            272,
            "2246847060",
            21.60
        )
        self.add_book(cetait_ca_ou_mourir)
        self.add_author(cetait_ca_ou_mourir.author)

        autre_cote_lac: Book = Book(
            "De l'autre côté du lac",
            Author(
                "Sylvain",
                "Prudhomme",
                47,
                "Sylvain Prudhomme est un écrivain français né en 1979. Voyageur et "
                "romancier, il s'intéresse aux territoires, aux rencontres, à la nature "
                "et aux personnes qui vivent en marge."
            ),
            "Près d'un lac de haute montagne, Paola, une photographe accompagnant des "
            "chercheurs, aperçoit quelque chose sur un versant. Après la découverte "
            "d'un corps, elle décide de rester seule dans la réserve avant de disparaître.",
            date(2026, 8, 27),
            "Les Éditions de Minuit",
            ["Paola", "le narrateur", "les chercheurs"],
            288,
            "2707358231",
            22.00
        )
        self.add_book(autre_cote_lac)
        self.add_author(autre_cote_lac.author)

        guerre_eternelle: Book = Book(
            "La Guerre éternelle",
            Author(
                "Olivier",
                "Rolin",
                79,
                "Olivier Rolin est un écrivain français né en 1947. Ancien militant "
                "politique, voyageur et reporter, il développe une œuvre marquée par "
                "l'histoire, les conflits, les paysages et la mémoire."
            ),
            "À partir de voyages, de souvenirs et de conflits anciens ou contemporains, "
            "le narrateur réfléchit à la permanence de la guerre dans l'histoire humaine "
            "et aux traces qu'elle laisse dans les paysages et les mémoires.",
            date(2026, 8, 20),
            "Gallimard",
            ["le narrateur", "les soldats", "les témoins"],
            352,
            "2073100678",
            22.50
        )
        self.add_book(guerre_eternelle)
        self.add_author(guerre_eternelle.author)

        bataille_au_proces: Book = Book(
            "Bataille au procès",
            Author(
                "Patrice",
                "Trigano",
                68,
                "Patrice Trigano est un écrivain, galeriste et spécialiste de l'art "
                "moderne. Ses livres mettent régulièrement en scène des artistes et "
                "interrogent les liens entre création, histoire et justice."
            ),
            "En 1956, Georges Bataille doit répondre de son œuvre devant la justice. "
            "Le roman met en scène le procès, les débats autour de la liberté littéraire "
            "et l'affrontement entre création artistique et morale publique.",
            date(2026, 8, 21),
            "Maurice Nadeau",
            ["Georges Bataille", "les magistrats", "les témoins"],
            192,
            "2862313599",
            19.00
        )
        self.add_book(bataille_au_proces)
        self.add_author(bataille_au_proces.author)


    def init_db(self):

        Book_dao : BookDao = BookDao()
        Author_dao : AuthorDao = AuthorDao()
        Member_dao : MemberDao = MemberDao()

        b = Book_dao.readAll()
        for book in b:
            self.add_book(book)
        a = Author_dao.readAll()
        for author in a:
            self.add_author(author)
        m = Member_dao.readAll()
        for member in m:
            self.add_member(member)


    def connection(self, email : str, pasword : str) -> str:
        status : ConnectionDao = ConnectionDao.sursh_status(email, pasword)
        return status
