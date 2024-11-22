# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtSql import QSqlDatabase

class SQLConnection:
    def __init__(self):
        self.dbConnection = QSqlDatabase.database()

        if not(self.dbConnection.isValid()):
            self.dbConnection = QSqlDatabase.addDatabase("QPSQL")
            self.dbConnection.setHostName("localhost")
            self.dbConnection.setDatabaseName("investments")
            self.dbConnection.setUserName("postgres")
            self.dbConnection.setPassword("1234")
            ok = self.dbConnection.open()
            if not self.dbConnection.isValid():
                print("Cannot add database")
            else:
                self.dbConnection = QSqlDatabase.database()
                print(f'resultado: {ok}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    SQLConnection()
    sys.exit(app.exec())
