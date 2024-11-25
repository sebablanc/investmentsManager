# This Python file uses the following encoding: utf-8
import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'seba',
    'password': 'investments',
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'investments',
    'raise_on_warnings': True,
    'auth_plugin': 'mysql_native_password'
}


class SQLConnection:
    def __init__(self):
        try:
          self.dbConnection = mysql.connector.connect(**config)
        except mysql.connector.Error as err:
            self.close()
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Acceso denegado a la base de datos")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def save(self, query, data):
        try:
            self.cursor = self.dbConnection.cursor()
            if(self.cursor):
                self.cursor.execute(query, data)
                self.dbConnection.commit()
                self.close()
        except Exception as e:
            print('Error al intentar guardar')
            print(e)

    def findAll(self, query):
        self.cursor = self.dbConnection.cursor()
        if(self.cursor):
            self.cursor.execute(query)

    def close(self):
        if self.dbConnection:
            self.cursor.close()
            self.dbConnection.close()
