from optparse import Option
from typing import Optional

from daos.dao import Dao


class ConnectionDao:
    def sursh_status(email : str, pasword :str) -> Optional[str]:
        try:
            with Dao.connection.cursor() as cursor:
                sql = "select u_statut from pg_user where u_email = %s AND u_pasword = %s"
                cursor.execute(sql, (email, pasword))
                record = cursor.fetchone()
                return record['u_statut']
        except Exception as e:
            print(f"Erreur lors de la connection : {e}")
            return None
