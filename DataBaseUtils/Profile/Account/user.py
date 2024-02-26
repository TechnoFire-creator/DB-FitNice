from DataBaseUtils.main import DataBase
class User(DataBase):
    """
    Gestion de l'utilisateur
    """
    def __init__(self):
        DataBase.__init__(self)
        self.create_table_user()
        self.table_name = "UsersAccounts"

    def create_table_user(self):
        """
        Crée la table UserAccounts
        :return:
        """
        table = """CREATE TABLE IF NOT EXISTS ? (
        	                    id INTEGER PRIMARY KEY AUTO_INCREMENT,
        	                    nom VARCHAR(100) NOT NULL,
        	                    prenom VARCHAR(100) NOT NULL,
        	                    date_naissance DATE,
        	                    sexe VARCHAR(1),
        	                    adresse_mail VARCHAR(255) NOT NULL,
        	                    telephone VARCHAR(255) NOT NULL,
        	                    adresse_postale VARCHAR(255) NOT NULL,
        	                    mots_passe TEXT NOT NULL,
        	                    description TEXT,
        	                    sport_pratique TEXT
                            );"""
        self.execute(table,(self.table_name,))  # Créer la DB

    def add_user(self,dico:dict):
        """
        Rajoute un utilisateur selon les info de la FronteEnd
        :param dico:
        :return:
        """
        self.execute("INSERT INTO ? ('nom','prenom','date_naissance','sexe','adresse_mail','telephone','adresse_postale','mots_passe','description','sport_pratique') VALUES (?,?,?,?,?,?,?,?,?,?)",(dico['nom'],dico['prenom'],dico['date_naissance'],dico['sexe'],dico['adresse_mail'],dico['telephone'],dico['adresse_postale'],dico['mots_passe'],dico['description'],dico['sport_pratique'],))

    def remove_user(self, id:int):
        """
        Supprime l'utilisateur
        :param id:
        :return:
        """
        self.execute("DELETE FROM ? WHERE ?",(self.table_name,id,))

    def is_user_existing(self,id:int):
        """
        Vérifie si l'utilisateur existe
        :return:
        """
        self.execute("SELECT COUNT(1) FROM ? WHERE id= ?;",(self.table_name,id,))
        result = self.cursor.fetchall()
        return True if result == 1 else False


    def modify_user(self):
        """
        Modifier les données de l'utilisateur
        :return:
        """
        pass

test = User()