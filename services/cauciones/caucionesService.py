# This Python file uses the following encoding: utf-8
from services.db.sqlconnection import SQLConnection

class CaucionesService:
    def __init__(self):
        self.db = SQLConnection()
