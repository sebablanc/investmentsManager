# This Python file uses the following encoding: utf-8
import sys
from datetime import datetime
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from cauciones.models.CaucionTableModel import CaucionTableModel

UI_FILE_NAME = "cauciones/caucionMain.ui"

class CaucionMain(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = self.loadCaucionMain()

        data = [
            [datetime(2024, 10, 7), 2000000.00, 30, 42.00, 2069041.1, 1700.58, 310.36, 422.30, 2066607.86, 66607.86, datetime(2026, 11, 6)],
            [1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 5, False, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        self.model = CaucionTableModel(data)

        self.ui.caucionesTable.setModel(self.model)

    def loadCaucionMain(self):
        ui_file = QFile(UI_FILE_NAME)
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {UI_FILE_NAME}: {ui_file.errorString()}")
            sys.exit(-1)

        loader = QUiLoader()
        return loader.load(ui_file)
