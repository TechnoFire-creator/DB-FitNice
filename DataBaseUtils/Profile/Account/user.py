from DataBaseUtils.main import Database

class User(Database):
    """
    Gestion de l'utilisateur
    """

    def __init__(self):
        super().__init__("../../database.db")
        self.create_table_user()

    def create_table_user(self):
        """
        Crée la table UserAccounts
        """
        table = """
        CREATE TABLE IF NOT EXISTS UsersAccounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom VARCHAR(100) NOT NULL,
            prenom VARCHAR(100) NOT NULL,
            date_naissance DATE,
            sexe VARCHAR(1),
            adresse_mail VARCHAR(255) NOT NULL UNIQUE,
            telephone VARCHAR(255) NOT NULL,
            adresse_postale VARCHAR(255) NOT NULL,
            mots_passe TEXT NOT NULL,
            description TEXT,
            sport_pratique TEXT
        );
        """
        self.execute(table)

    def get_table(self):
        """
        Montre la table
        :return: list
        """
        self.cursor.execute("SELECT * FROM UsersAccounts")
        return self.cursor.fetchall()

    def add_user(self, user_data: dict):
        """
        Rajoute un utilisateur selon les info de la FronteEnd
        :param user_data: dict (containing user information)
        """
        try:
            args = (user_data["nom"], user_data["prenom"], user_data["date_naissance"],
                    user_data["sexe"], user_data["adresse_mail"], user_data["telephone"],
                    user_data["adresse_postale"], user_data["mots_passe"],
                    user_data.get("description", ""), user_data.get("sport_pratique", ""))
            self.cursor.execute("INSERT OR IGNORE INTO UsersAccounts ('nom','prenom','date_naissance','sexe','adresse_mail','telephone','adresse_postale','mots_passe','description','sport_pratique') VALUES (?,?,?,?,?,?,?,?,?,?)", args)
            self.connection.commit()
        except Exception as e:
            print(f"Error adding user: {e}")

    def remove_user(self, user_id: int):
        """
        Supprime l'utilisateur
        :param user_id: int
        """
        try:
            self.cursor.execute("DELETE FROM UsersAccounts WHERE id = ?", (user_id,))
            self.connection.commit()
        except Exception as e:
            print(f"Error removing user: {e}")

    def modify_user(self, user_id: int, field_name: str, new_value: str):
        """
        Modifier les données de l'utilisateur.


        """
        try:
            self.cursor.execute(f"UPDATE UsersAccounts SET {field_name} = ? WHERE id = ?", (new_value, user_id))
            self.connection.commit()
        except Exception as e:
            print(f"Error modifying user: {e}")

# Example usage
test = User()
user_data = {
    "nom": "TestNom",
    "prenom": "TestPrenom",
    "date_naissance": "19/06/2000",
    "sexe": "H",
    "adresse_mail": "testemail@gmail.com",
    "telephone": "06 06 06 06 06 06",
    "adresse_postale": "52 av python",
    "mots_passe": "BGFDJBFIUDFB",
    "description": "testdesc",
    "sport_pratique": "Echec"
}

test.add_user(user_data)

print(test.get_table())


test.modify_user(1, "nom", "NewName")
print(test.get_table())
test.delete_db()
