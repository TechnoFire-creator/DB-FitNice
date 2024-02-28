import sqlite3
import os


class Database:

    def __init__(self, file_path: str):
        """
        Constructeur de la classe Database avec des fonctions prédéfini

        @param file_path: chemin du fichier
        @return
        """

        self.file_path = file_path
        self.connection = self.connect()
        self.cursor = self.connection.cursor()
        self._isExistDB()

    def _isExistDB(self) -> None:
        """
        Vérifier si la DB existe ou pas sinon on la créé
        @return
        """

        if os.path.exists(self.file_path):
            if not os.path.isfile(self.file_path):
                raise FileExistsError(f"Path '{self.file_path}' existe mais pas sous forme de fichier")
        else:
            open(self.file_path, 'x').close()  #

    def delete_db(self) -> None:
        """
        Supprime la base de donnée
        @return
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def connect(self) -> sqlite3.Connection:
        """
        Création d'une connection à la base de donné
        @return
        """
        connection = None
        try:
            connection = sqlite3.connect(self.file_path)
            return connection
        except Exception as e:
            print(e)

    def get_cursor(self) -> None:
        """
        Création d'un cursor sql
        @return
        """
        if not self.connection:
            self.connect()
        if not self.cursor:
            self.cursor = self.connection.cursor()
        return self.cursor

    def execute(self, statement_sql: str) -> None:
        """
        Fonction qui execute des instructions sql

        @param statement_sql string
        @return
        """

        try:
            self.cursor.execute(statement_sql)
            self.connection.commit()
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Impossible d'exécuter l'instruction: {e}")

    def close(self) -> None:
        """
        Fermer la bd
        @return
        """

        if self.connection:
            try:
                self.cursor.close()
                self.connection.close()
            except sqlite3.Error as e:
                raise sqlite3.Error(f"Impossible de fermer la connection {e}")

            self.connection = None
            self.cursor = None
