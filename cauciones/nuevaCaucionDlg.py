# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QDate, Signal, Slot
from utils.navigationUtils import NavigationUtils
from utils.calculatorUtils import CalculatorUtils

UI_FILE_NAME = "cauciones/nuevaCaucionDialog.ui"

class NuevaCaucionDlg(QDialog):
    def __init__(self, parent=None):
        super(NuevaCaucionDlg, self).__init__(parent)
        self.montoInversion = 0
        self.montoBruto = 0
        self.importeComision = 0
        self.importeDerechoMercado = 0
        self.importeIVA = 0
        self.days = 0
        self.tna = 0
        self.iva = 0
        self.porcentajeComision = 0
        self.porcentajeDerechoMercado = 0
        self.importeNetoReal = 0

        self.ui = self.loadNuevaCaucionDlg()

        # Conecta los eventos de la vista
        self.ui.currentDateInput.dateChanged.connect(self.dateChangedHandler)
        self.ui.daysInput.valueChanged.connect(self.daysChangedHandler)
        self.ui.tnaInput.valueChanged.connect(self.tnaChangedHandler)
        self.ui.montoInput.valueChanged.connect(self.montoChangedHandler)
        self.ui.comisionInput.valueChanged.connect(self.comisionChangedHandler)
        self.ui.derechoMercadoInput.valueChanged.connect(self.derechoMercadoChangedHandler)
        self.ui.cancelBtn.clicked.connect(parent.openWindow)

        # Setea el día actual al comienzo de la ventana
        self.ui.currentDateInput.setDate(QDate.currentDate())
        self.daysChangedHandler(0)


    # Setea el valor de la fecha de liquidación cuando se cambia la fecha,
    # teniendo en cuenta los días seleccionados
    def dateChangedHandler(self, value):
        self.ui.fechaLiquidacionLbl.setText(value.addDays(self.days).toString("dd/MM/yyyy"))
        self.recalcularTodoLosImportes()

    # Maneja el cambio de cantidad de días
    def daysChangedHandler(self, value = 0):
        # Setea el valor de la fecha de liquidación cuando se cambia los días seleccionado,
        # teniendo en cuenta la fecha seleccionada
        date = self.ui.currentDateInput.date()
        self.days = value
        self.ui.fechaLiquidacionLbl.setText(date.addDays(value).toString("dd/MM/yyyy"))

        self.recalcularTodoLosImportes()

    # Maneja el cambio de TNA
    def tnaChangedHandler(self, value):
        self.tna = value
        self.recalcularTodoLosImportes()

    # Maneja el cambio de monto
    def montoChangedHandler(self, value):
        self.montoInversion = value
        self.recalcularTodoLosImportes()


    # Maneja el cambio de monto
    def comisionChangedHandler(self, value):
        self.porcentajeComision = value
        self.recalcularTodoLosImportes()

    # Maneja el cambio de derecho de mercado
    def derechoMercadoChangedHandler(self, value):
        self.porcentajeDerechoMercado = value
        self.recalcularTodoLosImportes()

    def recalcularTodoLosImportes(self):
        # Setea el valor del monto bruto cuando se cambia los días seleccionado,
        # teniendo en cuenta la TNA y el monto seleccionados
        self.calcularImporteBrutoTna()

        #Recalcula el importe de comision
        self.calcularImporteComision()

        #Recalcula el importe de derecho de mercado
        self.calcularImporteDerechoMercado()

        # Recalcular el importe del IVA
        self.calcularImporteIVA()

        # Recalcular el importe Neto Real
        self.calcularImporteNetoReal()

        # Recalcular el importe de Ganancia Neta Real
        self.calcularImporteGananciaNetaReal()


    # Calcula, formatea y setea el importe bruto en el label correspondiente
    def calcularImporteBrutoTna(self):
        self.montoBruto = CalculatorUtils.montoResultanteTNA(self.montoInversion, self.tna, self.days)
        value = '%.2f' % self.montoBruto
        value = "$" + value.replace(".", ",")
        self.ui.montoImporteBrutoLbl.setText(value)

        self.calcularImporteComision()

    # Calcula, formatea y setea la comisión en el label correspondiente
    def calcularImporteComision(self,):
        self.importeComision = CalculatorUtils.calcularPorcentajePorDia(self.montoBruto, self.porcentajeComision, self.days)
        value = '%.2f' % self.importeComision
        value = "$" + value.replace(".", ",")
        self.ui.montoComisionesLbl.setText(value)

    # Calcula, formatea y setea la comisión en el label correspondiente
    def calcularImporteDerechoMercado(self):
        self.importeDerechoMercado = CalculatorUtils.calcularDerechoMercado(self.montoBruto, self.porcentajeDerechoMercado, self.days)
        value = '%.2f' % self.importeDerechoMercado
        value = "$" + value.replace(".", ",")
        self.ui.montoDerechoMercadoLbl.setText(value)

    # Calcula, formatea y setea el iva en el label correspondiente
    def calcularImporteIVA(self):
        self.importeIVA = CalculatorUtils.calcularIVA(self.importeComision+self.importeDerechoMercado)
        value = '%.2f' % self.importeIVA
        value = "$" + value.replace(".", ",")
        self.ui.montoIVALbl.setText(value)


    # Calcula, formatea y setea el importe neto real en el label correspondiente
    def calcularImporteNetoReal(self):
        self.importeNetoReal = self.montoBruto - self.importeComision - self.importeDerechoMercado - self.importeIVA
        value = '%.2f' % self.importeNetoReal
        value = "$" + value.replace(".", ",")
        self.ui.montoTotalLbl.setText(value)

    # Calcula, formatea y setea el importe de ganancia real en el label correspondiente
    def calcularImporteGananciaNetaReal(self):
        self.importeGananciaNetaReal = self.importeNetoReal - self.montoInversion
        value = '%.2f' % self.importeGananciaNetaReal
        value = "$" + value.replace(".", ",")
        self.ui.gananciaNetaLbl.setText(value)

    def loadNuevaCaucionDlg(self):
        navigator = NavigationUtils(UI_FILE_NAME)
        return navigator.loadNewWindow()
