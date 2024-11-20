# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(3840, 2160)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        MainWindow.setPalette(palette)
        MainWindow.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        MainWindow.setStyleSheet(u"background-color: \"black\";\n"
"color: \"white\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(800, 556))
        self.centralwidget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnCaucion = QPushButton(self.centralwidget)
        self.btnCaucion.setObjectName(u"btnCaucion")
        sizePolicy.setHeightForWidth(self.btnCaucion.sizePolicy().hasHeightForWidth())
        self.btnCaucion.setSizePolicy(sizePolicy)
        self.btnCaucion.setMinimumSize(QSize(150, 150))
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        self.btnCaucion.setFont(font)
        self.btnCaucion.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCaucion.setStyleSheet(u"background-color: \"green\";\n"
"color: \"white\";\n"
"margin: 10")

        self.gridLayout.addWidget(self.btnCaucion, 0, 0, 1, 1)

        self.btnFCI = QPushButton(self.centralwidget)
        self.btnFCI.setObjectName(u"btnFCI")
        sizePolicy.setHeightForWidth(self.btnFCI.sizePolicy().hasHeightForWidth())
        self.btnFCI.setSizePolicy(sizePolicy)
        self.btnFCI.setMinimumSize(QSize(150, 150))
        self.btnFCI.setFont(font)
        self.btnFCI.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnFCI.setStyleSheet(u"background-color: \"green\";\n"
"color: \"white\";\n"
"margin: 10;\n"
"")

        self.gridLayout.addWidget(self.btnFCI, 0, 1, 1, 1)

        self.btnBonos = QPushButton(self.centralwidget)
        self.btnBonos.setObjectName(u"btnBonos")
        sizePolicy.setHeightForWidth(self.btnBonos.sizePolicy().hasHeightForWidth())
        self.btnBonos.setSizePolicy(sizePolicy)
        self.btnBonos.setMinimumSize(QSize(150, 150))
        self.btnBonos.setFont(font)
        self.btnBonos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnBonos.setStyleSheet(u"background-color: \"green\";\n"
"color: \"white\";\n"
"margin: 10;")

        self.gridLayout.addWidget(self.btnBonos, 0, 2, 1, 1)

        self.btnONs = QPushButton(self.centralwidget)
        self.btnONs.setObjectName(u"btnONs")
        sizePolicy.setHeightForWidth(self.btnONs.sizePolicy().hasHeightForWidth())
        self.btnONs.setSizePolicy(sizePolicy)
        self.btnONs.setMinimumSize(QSize(150, 150))
        self.btnONs.setFont(font)
        self.btnONs.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnONs.setStyleSheet(u"background-color: \"green\";\n"
"color: \"white\";\n"
"margin: 10;")

        self.gridLayout.addWidget(self.btnONs, 1, 0, 1, 1)

        self.btnAcciones = QPushButton(self.centralwidget)
        self.btnAcciones.setObjectName(u"btnAcciones")
        sizePolicy.setHeightForWidth(self.btnAcciones.sizePolicy().hasHeightForWidth())
        self.btnAcciones.setSizePolicy(sizePolicy)
        self.btnAcciones.setMinimumSize(QSize(150, 150))
        self.btnAcciones.setFont(font)
        self.btnAcciones.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAcciones.setStyleSheet(u"background-color: \"green\";\n"
"color: \"white\";\n"
"margin: 10;")

        self.gridLayout.addWidget(self.btnAcciones, 1, 1, 1, 1)

        self.btnCedears = QPushButton(self.centralwidget)
        self.btnCedears.setObjectName(u"btnCedears")
        sizePolicy.setHeightForWidth(self.btnCedears.sizePolicy().hasHeightForWidth())
        self.btnCedears.setSizePolicy(sizePolicy)
        self.btnCedears.setMinimumSize(QSize(150, 150))
        self.btnCedears.setFont(font)
        self.btnCedears.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCedears.setStyleSheet(u"background-color: \"green\";\n"
"color: \"white\";\n"
"margin: 10;")

        self.gridLayout.addWidget(self.btnCedears, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.btnCartera = QPushButton(self.centralwidget)
        self.btnCartera.setObjectName(u"btnCartera")
        self.btnCartera.setMinimumSize(QSize(0, 65))
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(True)
        font1.setStrikeOut(False)
        font1.setKerning(False)
        self.btnCartera.setFont(font1)
        self.btnCartera.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCartera.setStyleSheet(u"background-color: \"green\";\n"
"color: \"white\";\n"
"margin: 10;")

        self.verticalLayout.addWidget(self.btnCartera)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Investments Manager", None))
        self.btnCaucion.setText(QCoreApplication.translate("MainWindow", u"Cauci\u00f3n", None))
        self.btnFCI.setText(QCoreApplication.translate("MainWindow", u"Fondos comunes\n"
" de inversi\u00f3n", None))
        self.btnBonos.setText(QCoreApplication.translate("MainWindow", u"Bonos", None))
        self.btnONs.setText(QCoreApplication.translate("MainWindow", u"Obligaciones\n"
"negociables", None))
        self.btnAcciones.setText(QCoreApplication.translate("MainWindow", u"Acciones", None))
        self.btnCedears.setText(QCoreApplication.translate("MainWindow", u"Cedears", None))
        self.btnCartera.setText(QCoreApplication.translate("MainWindow", u"Cartera", None))
    # retranslateUi

