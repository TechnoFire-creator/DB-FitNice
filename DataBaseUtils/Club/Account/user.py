from DataBaseUtils.main import Database


class Club(Database):
    """
    Gestion de l'utilisateur
    """

    def __init__(self):
        super().__init__("../../database.db")
        self.create_table_user()
        self.table_name = "UsersAccounts"

    def create_table_user(self) -> None:
        """
        Crée la table ClubsAccounts
        @return
        """
        table = """
        CREATE TABLE IF NOT EXISTS UsersAccounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom VARCHAR(100) NOT NULL,
            sport VARCHAR(255) NOT NULL,
			adresse VARCHAR(255) NOT NULL,
			description TEXT,
			nombre_joueurs INT NOT NULL,
			prix INT NOT NULL,
			niveau INT
        );
        """
        self.execute(table)

    def get_table(self) -> None:
        """
        Montre la table
        :return: list
        """
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        return self.cursor.fetchall()

    def add_user(self, user_data: dict) -> None:
        """
        Rajoute un club selon les infos de la FronteEnd
        @param user_data: dict (info du clubs)
        """
        try:
            args = (user_data["nom"], user_data["sport"], user_data["adresse"],
                    user_data.get("description",""), user_data["nombre_joueurs"], user_data["prix"],user_data.get)
            self.cursor.execute(
                f"INSERT OR IGNORE INTO {self.table_name} ('nom','sport','adresse', 'description', 'nombre_joueurs', 'prix') VALUES (?,?,?,?,?,?)",
                args)
            self.connection.commit()
        except Exception as e:
            print(f"Error adding club: {e}")

    def remove_user(self, user_id: int) -> None:
        """
        Supprime le clubs
        @param user_id: int
        """
        try:
            self.cursor.execute(f"DELETE FROM {self.table_name} WHERE id = ?", (user_id,))
            self.connection.commit()
        except Exception as e:
            print(f"Error removing club: {e}")

    def modify_club(self, user_id: int, field_name: str, new_value: str) -> None:
        """
        Modifier les données des clubs.

        @param user_id: int (identifiant)
        @param field_name: str (Un champ par exemple le nom)
        @param new_value: str (Une nouvelle valeur au champ)
        @return
        """
        try:
            self.cursor.execute(f"UPDATE {self.table_name} SET {field_name} = ? WHERE id = ?", (new_value, user_id))
            self.connection.commit()
        except Exception as e:
            print(f"Error modifying user: {e}")


# Example usage
test = Club()
user_data = {
    "nom": "TestNom",
    "sport": "voile",
    "adresse": "88 av des galaxies",
    "description": "testetstetststs",
    "nombre_joueurs": 10,
    "prix": 45
}


test.add_user(user_data)

print(test.get_table())

print(test.get_table())
test.remove_user(1)
print(test.get_table())
test.delete_db()
