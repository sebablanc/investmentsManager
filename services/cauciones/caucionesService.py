# This Python file uses the following encoding: utf-8
from datetime import datetime
from services.db.sqlconnection import SQLConnection
from PySide6.QtCore import QDate

ADD_CAUCION = ("INSERT INTO caucion "
"(fecha, monto, tna, comision, dias, derecho_mercado) "
"VALUES (%(fecha)s, %(monto)s, %(tna)s, %(comision)s, %(dias)s, %(derecho_mercado)s)")

UPDATE_CAUCION = ("UPDATE caucion SET "
"fecha = %(fecha)s, monto = %(monto)s, tna = %(tna)s, comision = %(comision)s, dias = %(dias)s, derecho_mercado = %(derecho_mercado)s "
"WHERE caucion_id = %(caucion_id)s")

FIND_ALL = ("SELECT * FROM caucion ORDER BY caucion_id DESC")

class CaucionesService:

    '''
        Guarda caución
    '''
    def save(self, fecha, monto, tna, comision, dias, derechoMercado):
        self.db = SQLConnection()
        data_caucion = {
          'fecha': fecha,
          'monto': monto,
          'tna': tna,
          'comision': comision,
          'dias': dias,
          'derecho_mercado': derechoMercado
        }
        self.db.save(ADD_CAUCION, data_caucion)

    '''
        Actualiza caución
    '''
    def update(self, caucionId, fecha, monto, tna, comision, dias, derechoMercado):
        print('llama al update')
        self.db = SQLConnection()
        data_caucion = {
          'fecha': fecha,
          'monto': monto,
          'tna': tna,
          'comision': comision,
          'dias': dias,
          'derecho_mercado': derechoMercado,
          'caucion_id': caucionId
        }
        print(data_caucion)
        self.db.save(UPDATE_CAUCION, data_caucion)

    '''
        Devuelve el listado completo
    '''
    def findAll(self):
        self.db = SQLConnection()
        self.db.findAll(FIND_ALL)
        dataToReturn = []
        for (caucion_id, fecha, monto, tna, comision, dias, derecho_mercado) in self.db.cursor:
            dataToReturn.append([QDate(fecha), monto, dias, tna, comision, derecho_mercado, caucion_id])
        return dataToReturn



