import sqlite3
import os
class DataBase:
    """
    Classe utilitaire permettant de gèrer l'utilisation de la base de donnée par les sous-classes
    """
    def __init__(self):
        self.file_path = '../../DataBase.db'
        self.create_db()
        self.connection = self.create_connection()
        self.cursor = self.connection.cursor()
    def create_db(self):
        """
        Creation de la base de donnée
        :return:
        """
        if not os.path.exists(self.file_path):
            with open(self.file_path,'x') as file:
                file.close()
    def delete_db(self):
        """
        Supprime la base de donnée
        :return:
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def create_connection(self):
        """
        Création d'une connection à la base de donné
        :return:
        """
        connection = None
        try:
            connection = sqlite3.connect(self.file_path)
            return connection
        except Exception as e:
            print(e)

        return connection

    def execute(self,statement_slq):
        """
        Création d'une table dans la bd selon la déclaration de l'utilisateur
        :param statement:
        :return:
        """
        try:
            self.cursor.execute(statement_slq)
        except Exception as e:
            print(e)
