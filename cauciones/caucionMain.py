# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget
from cauciones.models.CaucionTableModel import CaucionTableModel
from cauciones.nuevaCaucionDlg import NuevaCaucionDlg
from utils.navigationUtils import NavigationUtils
from services.cauciones.caucionesService import CaucionesService

UI_FILE_NAME = "cauciones/caucionMain.ui"

class CaucionMain(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = self.loadCaucionMain()
        self.caucionesSrv = CaucionesService()
        self.windowUi = NuevaCaucionDlg(self, self.openWindow)
        self.data = []
        self.getData()

        self.ui.nuevaCaucionBtn.clicked.connect(
                    lambda checked: self.openNuevaCaucionDlg()
                )

    def getData(self):
        try:
            self.data = self.caucionesSrv.findAll()
            self.populateTable()
        except Exception:
            self.data = []

    def populateTable(self):
        if(self.data):
            self.model = CaucionTableModel(self.data)

            self.ui.caucionesTable.setModel(self.model)
            self.ui.caucionesTable.resizeColumnsToContents()
            self.ui.caucionesTable.doubleClicked.connect(self.itemDoubleClicked)

    def itemDoubleClicked(self, value):
        if(self.data):
            dataToSend = self.data[value.row()]
            data_caucion = {
              'fecha': dataToSend[0],
              'monto': dataToSend[1],
              'tna': dataToSend[3],
              'comision': dataToSend[4],
              'dias': dataToSend[2],
              'derechoMercado': dataToSend[5],
              'caucion_id': dataToSend[6]
            }
            self.openNuevaCaucionDlg(data_caucion)

    def openNuevaCaucionDlg(self, data=None):
        self.windowUi.setCaucion(data)
        self.openWindow()

    def openWindow(self):
        if self.windowUi.ui.isVisible():
            self.windowUi.ui.hide()
            self.getData()
        else:
            self.windowUi.ui.show()

    def loadCaucionMain(self):
        navigator = NavigationUtils(UI_FILE_NAME)
        return navigator.loadNewWindow()
