from dataclasses import dataclass
from typing import Optional

from daos.dao import Dao
from models.Member import Member


@dataclass
class MemberDao(Dao[Member]):
    def create(self, member: Member) -> int:
        id_member : Optional[int]
        id_user : int
        id_person : int
        try:
            with Dao.connection.cursor() as cursor:
                sql_person = "INSERT INTO pg_person (p_surname, p_name, p_age) VALUES (%s, %s, %s)"
                cursor.execute(sql_person, (member.last_name, member.first_name, member.age))
                id_person = cursor.lastrowid

                sql_user = "INSERT INTO pg_user (p_ID_person, u_email, u_pasword, u_statut) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql_user, (id_person, member.email, member.password, member.statut))
                id_user = cursor.lastrowid

                sql_member = "INSERT INTO pg_member(u_ID_user, m_ID_membre) VALUES (%s, %s)"
                cursor.execute(sql_member, (id_user, member.member_nbr))
                id_membre = cursor.lastrowid
                Dao.connection.commit()
                return id_member
        except Exception as e:
            print(f"Erreur lors de la création du membre : {e}")
            Dao.connection.rollback()
            return 0

    def member_from_db(self, record)-> Member:
        member : Member = Member(record['p_surname'], record['p_name'], record['p_age'], record['u_emal'], record['u_pasword'], record['u_statut'] )
        return member

    def read(self, member_id: int) -> Member:
        member : Optional[Member]
        try:
            with Dao.connection.cursor() as cursor:
                sql_person = "SELECT * FROM pg_member M INNER JOIN pg_user U ON U.u_ID_user = M.u_ID_user INNER JOIN pg_person P ON U.p_ID_person = P.p_ID_person WHERE M.m_ID_membre = %s"
                cursor.execute(sql_person, (member_id,))
                record = cursor.fetchone()
                if record is not None:
                    member = self.member_from_db(record)
                else :
                    member = None
                return member
        except Exception as e:
            print(f"Erreur lors de la création du membre : {e}")

    def readAll(self) -> list[Member]:
        pass
    def update(self, member: Member) -> bool:
        pass
    def delete(self, member: Member) -> bool:
        pass
