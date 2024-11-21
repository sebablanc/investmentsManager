# This Python file uses the following encoding: utf-8

PORCENTAJE_IVA = 0.21
DIAS_ANIO = 365
PORCENTAJE_TOTAL = 100
DIAS_DERECHO_MERCADO = 90

class CalculatorUtils:
    def montoResultanteTNA(monto, tna, dias):
        tnaPorDia = tna / (DIAS_ANIO*PORCENTAJE_TOTAL)
        return monto * (1 + tnaPorDia * dias)

    def calcularPorcentajePorDia(monto, porcentaje, dias):
        porcentajePorDia = porcentaje / (DIAS_ANIO*PORCENTAJE_TOTAL)
        return monto * (porcentajePorDia * dias)

    def calcularDerechoMercado(monto, porcentaje, dias):
        porcentajePorDia = porcentaje / (DIAS_DERECHO_MERCADO * PORCENTAJE_TOTAL)
        return monto * (porcentajePorDia * dias)

    def calcularIVA(monto):
        return monto * PORCENTAJE_IVA
