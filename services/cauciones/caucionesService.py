# This Python file uses the following encoding: utf-8
from datetime import datetime
from services.db.sqlconnection import SQLConnection
from PySide6.QtCore import QDate

ADD_CAUCION = ("INSERT INTO caucion "
"(fecha, monto, tna, comision, dias) "
"VALUES (%(fecha)s, %(monto)s, %(tna)s, %(comision)s, %(dias)s)")

FIND_ALL = ("SELECT * FROM caucion ORDER BY caucion_id DESC")

class CaucionesService:

    '''
        Guarda cauciones
    '''
    def save(self, fecha, monto, tna, comision, dias, derechoMercado):
        self.db = SQLConnection()
        data_caucion = {
          'fecha': fecha,
          'monto': monto,
          'tna': tna,
          'comision': comision,
          'dias': dias,
          'derechoMercado': derechoMercado
        }
        self.db.save(ADD_CAUCION, data_caucion)

    '''
        Devuelve el listado completo
    '''
    def findAll(self):
        self.db = SQLConnection()
        self.db.findAll(FIND_ALL)
        dataToReturn = []
        for (caucion_id, fecha, monto, tna, comision, dias) in self.db.cursor:
            dataToReturn.append([QDate(fecha), monto, dias, tna, comision, caucion_id])
        return dataToReturn



