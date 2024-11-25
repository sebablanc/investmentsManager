# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
from mysql import connector

class SQLConnection:
    def __init__(self):
        self.dbConnection = connector.connect(
                host="127.0.0.1",
                database="investments",
                user="seba",
                password="Seba_1234")

        print(self.dbConnection.cursor())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    SQLConnection()
    sys.exit(app.exec())
