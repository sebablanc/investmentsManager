# This Python file uses the following encoding: utf-8
from datetime import datetime
from PySide6.QtWidgets import QWidget
from cauciones.models.CaucionTableModel import CaucionTableModel
from cauciones.nuevaCaucionDlg import NuevaCaucionDlg
from utils.navigationUtils import NavigationUtils

UI_FILE_NAME = "cauciones/caucionMain.ui"

class CaucionMain(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = self.loadCaucionMain()

        data = [
            [datetime(2024, 10, 7), 2000000.00, 30, 42.00, 2069041.1, 1700.58, 310.36, 422.30, 2066607.86, 66607.86, datetime(2024, 11, 6)],
            [1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 5, False, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        self.model = CaucionTableModel(data)

        self.ui.caucionesTable.setModel(self.model)

        self.ui.nuevaCaucionBtn.clicked.connect(
                    lambda checked: self.openNuevaCaucionDlg()
                )

    def openNuevaCaucionDlg(self):
        self.windowUi = NuevaCaucionDlg(self)
        self.openWindow()

    def openWindow(self):
        if self.windowUi.ui.isVisible():
            self.windowUi.ui.hide()
        else:
            self.windowUi.ui.show()

    def loadCaucionMain(self):
        navigator = NavigationUtils(UI_FILE_NAME)
        return navigator.loadNewWindow()
