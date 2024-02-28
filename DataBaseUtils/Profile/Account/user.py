from DataBaseUtils.main import Database
from friends import Friend

class User(Database):
    """
    Gestion de l'utilisateur
    """

    def __init__(self):
        super().__init__("../../database.db")
        self.create_table_user()
        self.table_name = "UsersAccounts"

    def create_table_user(self) -> None:
        """
        Crée la table UserAccounts
        @return
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
            code_postal VARCHAR(255) NOT NULL,
            mots_passe TEXT NOT NULL,
            description TEXT,
            sport_pratique TEXT,
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
        Rajoute un utilisateur selon les info de la FronteEnd
        @param user_data: dict (info de l'utilisateur)
        """
        try:
            args = (user_data["nom"], user_data["prenom"], user_data["date_naissance"],
                    user_data["sexe"], user_data["adresse_mail"], user_data["telephone"],
                    user_data["code_postal"], user_data["mots_passe"],
                    user_data.get("description", ""), user_data.get("sport_pratique", ""), user_data.get("niveau",0))
            self.cursor.execute(
                f"INSERT OR IGNORE INTO {self.table_name} ('nom','prenom','date_naissance','sexe','adresse_mail','telephone','code_postal','mots_passe','description','sport_pratique',niveau) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                args)
            self.connection.commit()
        except Exception as e:
            print(f"Error adding user: {e}")

    def remove_user(self, user_id: int) -> None:
        """
        Supprime l'utilisateur
        @param user_id: int
        """
        try:
            self.cursor.execute(f"DELETE FROM {self.table_name} WHERE id = ?", (user_id,))
            friendlink = Friend()
            friendlink.remove_user(user_id)
            self.connection.commit()
        except Exception as e:
            print(f"Error removing user: {e}")

    def modify_user(self, user_id: int, field_name: str, new_value: str) -> None:
        """
        @summary Modifier les données de l'utilisateur.

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

    def search_user(self, code_postal: str = None, niveau_min: int = 0, niveau_max: int = 3, sexe: str = None):
        """
        @summary: chercher des utilisateurs selon leur code postal, sport, niveau et genre

        @param code_postal: str
        @param niveau_min: int (défaut 0)
        @param niveau_max: int (défaut 3)
        @param sexe: str
        @retun list: de utilisateur selon les filtres
        """
        # Construction de la clause WHERE dynamique
        where_clauses = []
        if code_postal:
            where_clauses.append(f"code_postal = '{code_postal}'")
        where_clauses.append(f"niveau BETWEEN {niveau_min} AND {niveau_max}")
        if sexe:
            where_clauses.append(f"sexe = '{sexe}'")

        # Jointure des clauses WHERE avec AND
        where_clause = " AND ".join(where_clauses) if where_clauses else "1=1"

        # Execution de la requête
        query = f"SELECT * FROM {self.table_name} WHERE {where_clause}"
        self.cursor.execute(query)
        return self.cursor.fetchall()


# Example usage
test = User()
user_data = {
    "nom": "TestNom",
    "prenom": "TestPrenom",
    "date_naissance": "19/06/2000",
    "sexe": "F",
    "adresse_mail": "testemail@gmail.com",
    "telephone": "06 06 06 06 06 06",
    "code_postal": "06220",
    "mots_passe": "BGFDJBFIUDFB",
    "description": "testdesc",
    "sport_pratique": "Echec",
    "niveau" : 0
}
user_data2 = {
    "nom": "TestNom2",
    "prenom": "TestPrenom2",
    "date_naissance": "19/06/2000",
    "sexe": "H",
    "adresse_mail": "test2email@gmail.com",
    "telephone": "06 02 06 06 06 06",
    "code_postal": "06220",
    "mots_passe": "BGFDJBFIUDFB222",
    "description": "testdesc2",
    "sport_pratique": "Echec",
    "niveau": 4
}
user_data3 = {
    "nom": "TestNom3",
    "prenom": "TestPrenom3",
    "date_naissance": "19/06/2000",
    "sexe": "H",
    "adresse_mail": "test3email@gmail.com",
    "telephone": "06 02 06 06 06 06",
    "code_postal": "62520",
    "mots_passe": "BGFDJBFIUDFB333",
    "description": "testdesc3",
    "sport_pratique": "Echec",
    "niveau": 2
}
test.add_user(user_data)
test.add_user(user_data2)
test.add_user(user_data3)


print(test.search_user(code_postal="06220",niveau_min=0,niveau_max=4))