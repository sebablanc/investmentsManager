# This Python file uses the following encoding: utf-8


class CaucionModel:
    def __init__(self, data):
        self.id = data['caucion_id'] if data and data['caucion_id'] else None
        self.fechaInicio = data['fecha'] if data and data['fecha'] else None
        self.montoInversion = data['monto'] if data and data['monto'] else 0
        self.montoBruto = 0
        self.importeComision = 0
        self.importeDerechoMercado = 0
        self.importeIVA = 0
        self.days = data['dias'] if data and data['dias'] else 0
        self.tna = data['tna'] if data and data['tna'] else 0
        self.iva = 0
        self.porcentajeComision = data['comision'] if data and data['comision'] else 0
        self.porcentajeDerechoMercado = data['derechoMercado'] if data and data['derechoMercado'] else 0
        self.importeNetoReal = 0
