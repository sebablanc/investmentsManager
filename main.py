# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QCoreApplication, Qt
from cauciones.caucionMain import CaucionMain
from fci.fciMain import FciMain
from utils.navigationUtils import NavigationUtils

UI_FILE_NAME = "mainwindow.ui"

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.subwindow = None

        self.ui = self.loadMainWindow()

        self.ui.showMaximized()

        self.ui.btnCaucion.clicked.connect(
                    lambda checked: self.switchWindow(1)
                )

        self.ui.btnFCI.clicked.connect(
                    lambda checked: self.switchWindow(2)
                )

    def loadMainWindow(self):
        navigator = NavigationUtils(UI_FILE_NAME)
        return navigator.loadNewWindow()

    def switchWindow(self, index):
        if index == 1:
            self.subwindow = CaucionMain()
        elif index == 2:
            self.subwindow = FciMain()

        self.openWindow(self.subwindow.ui)

    def openWindow(self, windowUi):
        if windowUi.isVisible():
            windowUi.hide()
        else:
            windowUi.showMaximized()

if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.ui.show()
    sys.exit(app.exec())
