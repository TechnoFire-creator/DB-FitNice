from typing import List, Dict, Any

from DataBaseUtils.main import Database


class Friend(Database):
    """
    Gestion de l'utilisateur
    """

    def __init__(self):
        super().__init__("../../database.db")
        self.create_table_user()
        self.table_name = "Friends"

    def create_table_user(self) -> None:
        """
        Crée la table Friend
        @return
        """
        table = """
        CREATE TABLE IF NOT EXISTS Friends (
           IDU1 INTEGER,
		   IDU2 INTEGER,
		   date_amitie DATE,
		   statut VARCHAR(100),
		   FOREIGN KEY (IDU1) REFERENCES UsersAccounts(id),
		   FOREIGN KEY (IDU2) REFERENCES UsersAccounts(id)
        );
        """
        self.execute(table)

    def get_table(self) -> list:
        """
        Montre la table
        @return list contenant la table
        """
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        return self.cursor.fetchall()

    def get_friends(self,id_user1:int,) -> list[dict[str, Any]]:
        """
        Récupérer les amis d'un utilisateur
        @param id_user1: int (Identifiant utilisateur 1)
        @return dico contenant les amis de user
        """
        commmand = f"SELECT * FROM Friends f INNER JOIN UsersAccounts u ON u.id = f.IDU1 WHERE f.IDU1 = {id_user1} AND f.statut = 'ami'"
        self.execute(commmand)
        results = self.cursor.fetchall()

        # Traitement des résultats
        amis = []
        for row in results:
            amis.append({
                "nom": row[0],
                "prenom": row[1],
                "date_amitie": row[2],
                "statut": row[3],
            })

        return amis

    def add_user(self, user_id: int,friend_id: int, date: str) -> None:
        """
        Rajoute un lien d'amitié selon les info de la FronteEnd

        @param user_id: int
        @param friend_id: int
        @param date: int
        @return
        """
        try:
            args = (user_id,friend_id,date,"ami")
            self.cursor.execute(
                f"INSERT INTO {self.table_name} ('IDU1', 'IDU2', 'date_amitie', 'statut') VALUES (?, ?, ?, ?);",
                args)
            self.connection.commit()
        except Exception as e:
            print(f"Error adding friend: {e}")

    def remove_user(self, id:int) -> None:
        """
        Supprier tout les liens avec l'utilisateurs
        @param id: int
        @return:

        """
        try:
            self.cursor.execute(f"DELETE FROM {self.table_name} WHERE IDU1 = {id} ")
            self.connection.commit()
        except Exception as e:
            print(f"Error removing friend: {e}")

    def remove_user_link(self, user_id: int,friend_id: int) -> None:
        """
        Supprime le liens d'amitié entre ses deux personnes
        @param user_id: int
        @param friend_id: int
        """
        try:
            self.cursor.execute(f"DELETE FROM {self.table_name} WHERE IDU1 = {user_id} AND IDU2 = {friend_id}")
            self.connection.commit()
        except Exception as e:
            print(f"Error removing friend: {e}")

    def modify_friend_info(self, user_id: int, friend_id:int, field_name: str, new_value: str) -> None:
        """
        Modifier les données de l'amitié seulement statut.
        statut : Statut de l'amitié (ami, en_attente, bloqué).


        @param user_id: int (identifiant)
        @param field_name: str (Un champ par exemple le nom)
        @param new_value: str (Une nouvelle valeur au champ)
        @return
        """
        try:
            self.cursor.execute(f"UPDATE UsersAccounts SET {field_name} = {new_value} WHERE IDU1 = {user_id} AND IDU2 = {friend_id}")
            self.connection.commit()
        except Exception as e:
            print(f"Error modifying friend link info: {e}")

