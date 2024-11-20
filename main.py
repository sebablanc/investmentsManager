# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from cauciones.caucionMain import CaucionMain

UI_FILE_NAME = "mainwindow.ui"

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.window1 = CaucionMain()

        self.ui = self.loadMainWindow()

        self.ui.btnCaucion.clicked.connect(
                    lambda checked: self.openWindow(self.window1)
                )

    def loadMainWindow(self):
        ui_file = QFile(UI_FILE_NAME)
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {UI_FILE_NAME}: {ui_file.errorString()}")
            sys.exit(-1)

        loader = QUiLoader()
        return loader.load(ui_file)

    def openWindow(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.ui.show()
    sys.exit(app.exec())
