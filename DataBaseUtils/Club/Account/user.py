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
			code_postal VARCHAR(255) NOT NULL,
			description TEXT,
			nombre_joueurs INT NOT NULL,
			prix INT NOT NULL,
			niveau_moy INT
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
            args = (user_data["nom"], user_data["sport"], user_data["code_postal"],
                    user_data.get("description",""), user_data["nombre_joueurs"], user_data["prix"],user_data["niveau_moy"])
            self.cursor.execute(
                f"INSERT OR IGNORE INTO {self.table_name} ('nom','sport','code_postal', 'description', 'nombre_joueurs', 'prix','niveau_moy') VALUES (?,?,?,?,?,?,?)",
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

    Fonction
    search_clubs
    avec
    filtre
    sur
    le
    prix
    Python

    def search_clubs(self, code_postal: str = None, niveau_min: int = 0, niveau_max: int = 3,
                     sport: str = None, prix: int = None, prix_operator: str = None):
        """
        @summary: chercher des clubs selon leur code postal, sport, niveau, prix et genre

        @param code_postal: str
        @param niveau_min: int (défaut 0)
        @param niveau_max: int (défaut 3)
        @param sport: str
        @param prix: int
        @param prix_operator: str ("< ou > ou = ou >= etc)
        @retun list: de clubs selon les filtres
        """
        # Construction de la clause WHERE dynamique
        where_clauses = []
        if code_postal:
            where_clauses.append(f"code_postal = '{code_postal}'")
        where_clauses.append(f"niveau BETWEEN {niveau_min} AND {niveau_max}")
        if sport:
            where_clauses.append(f"sport = '{sport}'")
        if prix is not None:
            if prix_operator not in ["<", ">", "=", "<=", ">="]:
                raise ValueError("Opérateur de prix invalide. Les options valides sont : <, >, =, <=, >=")
            where_clauses.append(f"prix {prix_operator} {prix}")

        # Jointure des clauses WHERE avec AND
        where_clause = " AND ".join(where_clauses) if where_clauses else "1=1"

        # Execution de la requête
        query = f"SELECT * FROM {self.table_name} WHERE {where_clause}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

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


