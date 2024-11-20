# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QDialog

UI_FILE_NAME = "cauciones/nuevaCaucionDialog.ui"

class NuevaCaucionDlg(QDialog):
    def __init__(self, parent=None):
        super(NuevaCaucionDlg, self).__init__(parent)
        self.ui = self.loadNuevaCaucionDlg()

    def loadNuevaCaucionDlg(self):
        ui_file = QFile(UI_FILE_NAME)
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {UI_FILE_NAME}: {ui_file.errorString()}")
            sys.exit(-1)

        loader = QUiLoader()
        return loader.load(ui_file)
