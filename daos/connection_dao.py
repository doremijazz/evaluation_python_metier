"""Accès aux données nécessaire à l'authentification."""
from optparse import Option
from typing import Optional

from daos.dao import Dao


class ConnectionDao:
    """Rechercher le statut associé à des identifiants de connexion."""
    def sursh_status(email : str, pasword :str) -> Optional[str]:
        """Retourner le statut de l'utilisateur correspondant.

        Args:
            email: Courriel saisi.
            pasword: Mot de passe saisi (nom historique conservé).

        Returns:
            Statut de l'utilisateur ou ``None`` si la connexion échoue.
        """
        try:
            with Dao.connection.cursor() as cursor:
                sql = "select u_statut from pg_user where u_email = %s AND u_pasword = %s"
                cursor.execute(sql, (email, pasword))
                record = cursor.fetchone()
                return record['u_statut']
        except Exception as e:
            print(f"Erreur lors de la connection : {e}")
            return None
