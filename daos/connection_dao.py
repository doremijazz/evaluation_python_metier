from optparse import Option
from typing import Optional

from daos.dao import Dao


class ConnectionDao:
    def sursh_status(email : str, pasword :str) -> Optional[str]:
        try:
            with Dao.connection.cursor() as cursor:
                sql = "select u_status from pg_users where email = %s AND pasword = %s"
                cursor.execute(sql, (email, pasword))
                status = cursor.fetchone()
                return status
        except Exception as e:
            print(f"Erreur lors de la connection : {e}")
            return None
