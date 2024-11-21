# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader

class NavigationUtils:
    def __init__(self, fileName):
        self.fileName = fileName

    def loadNewWindow(self):
        ui_file = QFile(self.fileName)
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {self.fileName}: {ui_file.errorString()}")
            sys.exit(-1)

        loader = QUiLoader()
        return loader.load(ui_file)
