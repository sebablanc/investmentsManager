# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader

UI_FILE_NAME = "fci/fciMain.ui"

class FciMain(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = self.loadFciMain()

    def loadFciMain(self):
        ui_file = QFile(UI_FILE_NAME)
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {UI_FILE_NAME}: {ui_file.errorString()}")
            sys.exit(-1)

        loader = QUiLoader()
        return loader.load(ui_file)
