# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QDate, QTimer
from cauciones.models.caucionModel import CaucionModel
from utils.navigationUtils import NavigationUtils
from utils.calculatorUtils import CalculatorUtils
from services.cauciones.caucionesService import CaucionesService

UI_FILE_NAME = "cauciones/nuevaCaucionDialog.ui"

class NuevaCaucionDlg(QDialog):
    def __init__(self, parent=None, onClose=None):
        super(NuevaCaucionDlg, self).__init__(parent)

        self.ui = self.loadNuevaCaucionDlg()
        self.caucionesSrv = CaucionesService()
        self.onClose = onClose
        self.caucion = CaucionModel(None)

        # Conecta los eventos de la vista
        self.ui.currentDateInput.dateChanged.connect(self.dateChangedHandler)
        self.ui.daysInput.valueChanged.connect(self.daysChangedHandler)
        self.ui.tnaInput.valueChanged.connect(self.tnaChangedHandler)
        self.ui.montoInput.valueChanged.connect(self.montoChangedHandler)
        self.ui.comisionInput.valueChanged.connect(self.comisionChangedHandler)
        self.ui.derechoMercadoInput.valueChanged.connect(self.derechoMercadoChangedHandler)
        self.ui.cancelBtn.clicked.connect(parent.openWindow)
        self.ui.saveBtn.clicked.connect(lambda a: self.guardarCaucion() if self.caucion.id is None else self.actualizarCaucion())

        # Setea el día actual al comienzo de la ventana
        self.ui.currentDateInput.setDate(QDate.currentDate())
        self.daysChangedHandler(0)

    def setCaucion(self, data):
        self.caucion = CaucionModel(data)
        self.ui.currentDateInput.setDate(self.caucion.fechaInicio)
        self.ui.montoInput.setValue(self.caucion.montoInversion)
        self.ui.tnaInput.setValue(self.caucion.tna)
        self.ui.daysInput.setValue(self.caucion.days)
        self.ui.comisionInput.setValue(self.caucion.porcentajeComision)
        self.ui.derechoMercadoInput.setValue(self.caucion.porcentajeDerechoMercado)
        self.recalcularTodoLosImportes()

    def guardarCaucion(self):
        self.enableBtn(False)
        try:
            self.caucionesSrv.save(
                self.caucion.fechaInicio.toString("yyyy-MM-dd"),
                self.caucion.montoInversion,
                self.caucion.tna,
                self.caucion.porcentajeComision,
                self.caucion.days,
                self.caucion.porcentajeDerechoMercado)
        except Exception as e:
            print(e)
        else:
            self.enableBtn(True)
            self.ui.hide()
            self.parent.getData()

    def actualizarCaucion(self):
        self.enableBtn(False)
        try:
            print('entra al actualizar')
            self.caucionesSrv.update(
                self.caucion.id,
                self.caucion.fechaInicio.toString("yyyy-MM-dd"),
                self.caucion.montoInversion,
                self.caucion.tna,
                self.caucion.porcentajeComision,
                self.caucion.days,
                self.caucion.porcentajeDerechoMercado)
        except Exception as e:
            print(e)
        finally:
            self.enableBtn(True)
            if(self.onClose is not None):
                self.onClose()

    def enableBtn(self, enable = True):
        self.ui.saveBtn.setEnabled(enable)

    # Setea el valor de la fecha de liquidación cuando se cambia la fecha,
    # teniendo en cuenta los días seleccionados
    def dateChangedHandler(self, value):
        self.caucion.fechaInicio = value
        self.ui.fechaLiquidacionLbl.setText(value.addDays(self.caucion.days).toString("dd/MM/yyyy"))
        self.recalcularTodoLosImportes()

    # Maneja el cambio de cantidad de días
    def daysChangedHandler(self, value = 0):
        # Setea el valor de la fecha de liquidación cuando se cambia los días seleccionado,
        # teniendo en cuenta la fecha seleccionada
        date = self.ui.currentDateInput.date()
        self.caucion.days = value
        self.ui.fechaLiquidacionLbl.setText(date.addDays(value).toString("dd/MM/yyyy"))

        self.recalcularTodoLosImportes()

    # Maneja el cambio de TNA
    def tnaChangedHandler(self, value):
        self.caucion.tna = value
        self.recalcularTodoLosImportes()

    # Maneja el cambio de monto
    def montoChangedHandler(self, value):
        self.caucion.montoInversion = value
        self.recalcularTodoLosImportes()


    # Maneja el cambio de monto
    def comisionChangedHandler(self, value):
        self.caucion.porcentajeComision = value
        self.recalcularTodoLosImportes()

    # Maneja el cambio de derecho de mercado
    def derechoMercadoChangedHandler(self, value):
        self.caucion.porcentajeDerechoMercado = value
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
        self.caucion.montoBruto = CalculatorUtils.montoResultanteTNA(self.caucion.montoInversion, self.caucion.tna, self.caucion.days)
        value = '%.2f' % self.caucion.montoBruto
        value = "$" + value.replace(".", ",")
        self.ui.montoImporteBrutoLbl.setText(value)

    # Calcula, formatea y setea la comisión en el label correspondiente
    def calcularImporteComision(self,):
        self.caucion.importeComision = CalculatorUtils.calcularPorcentajePorDia(self.caucion.montoBruto, self.caucion.porcentajeComision, self.caucion.days)
        value = '%.2f' % self.caucion.importeComision
        value = "$" + value.replace(".", ",")
        self.ui.montoComisionesLbl.setText(value)

    # Calcula, formatea y setea la comisión en el label correspondiente
    def calcularImporteDerechoMercado(self):
        self.caucion.importeDerechoMercado = CalculatorUtils.calcularDerechoMercado(self.caucion.montoBruto, self.caucion.porcentajeDerechoMercado, self.caucion.days)
        value = '%.2f' % self.caucion.importeDerechoMercado
        value = "$" + value.replace(".", ",")
        self.ui.montoDerechoMercadoLbl.setText(value)

    # Calcula, formatea y setea el iva en el label correspondiente
    def calcularImporteIVA(self):
        self.caucion.importeIVA = CalculatorUtils.calcularIVA(self.caucion.importeComision+self.caucion.importeDerechoMercado)
        value = '%.2f' % self.caucion.importeIVA
        value = "$" + value.replace(".", ",")
        self.ui.montoIVALbl.setText(value)


    # Calcula, formatea y setea el importe neto real en el label correspondiente
    def calcularImporteNetoReal(self):
        self.caucion.importeNetoReal = self.caucion.montoBruto - self.caucion.importeComision - self.caucion.importeDerechoMercado - self.caucion.importeIVA
        value = '%.2f' % self.caucion.importeNetoReal
        value = "$" + value.replace(".", ",")
        self.ui.montoTotalLbl.setText(value)

    # Calcula, formatea y setea el importe de ganancia real en el label correspondiente
    def calcularImporteGananciaNetaReal(self):
        self.caucion.importeGananciaNetaReal = self.caucion.importeNetoReal - self.caucion.montoInversion
        value = '%.2f' % self.caucion.importeGananciaNetaReal
        value = "$" + value.replace(".", ",")
        self.ui.gananciaNetaLbl.setText(value)

    def loadNuevaCaucionDlg(self):
        navigator = NavigationUtils(UI_FILE_NAME)
        return navigator.loadNewWindow()
