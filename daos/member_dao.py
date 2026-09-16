from dataclasses import dataclass
from typing import Optional

from daos.dao import Dao
from models.Member import Member
from models.Person import Person


@dataclass
class MemberDao(Dao[Member]):
    def create(self, member: Member) -> int:
        id_member : Optional[int]
        id_user : int
        id_person : int
        #print("avant try")
        try:
            with Dao.connection.cursor() as cursor:
                sql_person = "INSERT INTO pg_person (p_surname, p_name, p_age) VALUES (%s, %s, %s)"
                cursor.execute(sql_person, (member.last_name, member.first_name, member.age))
                id_person = cursor.lastrowid
                Person.id_person = id_person

                #print(f"id_person : {id_person}")

                sql_user = "INSERT INTO pg_user (p_ID_person, u_email, u_pasword, u_statut) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql_user, (id_person, member.email, member.password, member.statut))
                id_user = cursor.lastrowid

                #print(f"id_user : {id_user}")

                sql_member = "INSERT INTO pg_membre (u_ID_user) VALUES (%s)"
                cursor.execute(sql_member, (id_user, ))

                id_membre = cursor.lastrowid
                member.member_nbr : int = id_membre

                #print(f"id_membre : {id_membre}")

                Dao.connection.commit()
                return id_membre
        except Exception as e:
            print(f"Erreur lors de la création du membre : {e}")
            Dao.connection.rollback()
            return 0

    def member_from_db(self, record)-> Member:
        member : Member = Member(record['p_surname'], record['p_name'], record['p_age'], record['u_email'], record['u_pasword'], record['u_statut'] )
        member.member_nbr = record['m_ID_membre']
        return member

    def read(self, member_id: int) -> Member:
        member : Optional[Member]
        try:
            with Dao.connection.cursor() as cursor:
                sql_person = "SELECT * FROM pg_membre M INNER JOIN pg_user U ON U.u_ID_user = M.u_ID_user INNER JOIN pg_person P ON U.p_ID_person = P.p_ID_person WHERE M.m_ID_membre = %s"
                cursor.execute(sql_person, (member_id,))
                record = cursor.fetchone()
                if record is not None:
                    member = self.member_from_db(record)
                else :
                    member = None
                return member
        except Exception as e:
            print(f"Erreur lors de la lecture du membre : {e}")

    def readAll(self) -> list[Member]:
        member_list : list[Member] = []
        try:
            with Dao.connection.cursor() as cursor:
                sql = "SElECT * FROM pg_membre M INNER JOIN pg_user U ON U.u_ID_user = M.u_ID_user INNER JOIN pg_person P ON U.p_ID_person = P.p_ID_person"
                cursor.execute(sql)
                records = cursor.fetchall()
                for record in records:
                    member_list.append(self.member_from_db(record))
                return member_list
        except Exception as e:
            print(f"Erreur lors de la lecture des membres : {e}")

    def update(self, member: Member) -> bool:
        try:
            with Dao.connection.cursor() as cursor:
                sql_person = ("UPDATE pg_person P JOIN pg_user U ON U.p_ID_person = P.p_ID_person JOIN "
                              "pg_member ON U.u_ID_user = M.u_ID_user SET P.p_surname = %s, "
                              "P.p_name = %s, P.p_age = %s, U.u_email = %s, U.u_pasword = %s, U.u_statut = %s "
                              " WHERE M.m_ID_membre = %s")
                cursor.execute(sql_person, (member.last_name, member.first_name, member.age, member.email, member.password, member.statut, member.member_nbr))
                return True
        except Exception as e:
            print(f"Erreur lors de la mise ajour du membre : {e}")
            return False

    def delete(self, member: Member) -> bool:
        try:
            with Dao.connection.cursor() as cursor:
                sql_selec_person = ("SELECT P.p_ID_person FROM pg_person AS P "
                                    "INNER JOIN pg_user U ON U.p_ID_person = P.p_ID_person "
                                    "INNER JOIN pg_membre M ON U.u_ID_user = M.u_ID_user "
                                    "WHERE M.m_ID_membre = %s")
                cursor.execute(sql_selec_person, (member.member_nbr,))
                record = cursor.fetchone()
                id_person : int = record["p_ID_person"]
                #print("id_person : ", id_person)
                sql_member = "DELETE FROM pg_membre WHERE m_ID_membre = %s"
                cursor.execute(sql_member, (member.member_nbr,))
                id_membre = cursor.lastrowid
                #print("delete membre : ", id_membre)
                sql_increment_member = "ALTER TABLE pg_membre AUTO_INCREMENT = %s"
                cursor.execute(sql_increment_member, (id_membre,))

                sql_user = "DELETE FROM pg_user WHERE p_ID_person = %s"
                cursor.execute(sql_user, (id_person,))
                id_user = cursor.lastrowid
                #print("delete user : ", id_user)
                sql_increment_user = "ALTER TABLE pg_user AUTO_INCREMENT = %s"
                cursor.execute(sql_increment_user, (id_user,))

                sql_person = "DELETE FROM pg_person WHERE p_ID_person = %s"
                cursor.execute(sql_person, (id_person,))
                #print("delete person : ", id_person)


                sql_increment_person = "ALTER TABLE pg_person AUTO_INCREMENT = %s"
                cursor.execute(sql_increment_person, (id_person,))

                Dao.connection.commit()
                return True
        except Exception as e:
            print(f"Erreur lors de la supression du membre : {e}")
            Dao.connection.rollback()
            return False

    def sursh(self, name: str, surname : str) -> Optional[Member]:
        try:
            with Dao.connection.cursor() as cursor:
                sql = "SELECT * FROM pg_membre WHERE m_first_name = %s AND m_last_name = %s"
                cursor.execute(sql, (name, surname))
                record = cursor.fetchone()
                member = self.member_from_db(record)
                return member
        except Exception as e:
            print(f"Erreur lors du membre : {e}")
            Dao.connection.rollback()
            return None
