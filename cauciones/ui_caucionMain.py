# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'caucionMain.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_caucionesWidget(object):
    def setupUi(self, caucionesWidget):
        if not caucionesWidget.objectName():
            caucionesWidget.setObjectName(u"caucionesWidget")
        caucionesWidget.resize(1080, 730)
        caucionesWidget.setStyleSheet(u"background-color: \"black\";\n"
"color: \"white\";")
        self.verticalLayout = QVBoxLayout(caucionesWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.caucionesTable = QTableView(caucionesWidget)
        self.caucionesTable.setObjectName(u"caucionesTable")
        self.caucionesTable.setStyleSheet(u"background: \"lightgray\"; color: \"black\"")

        self.verticalLayout.addWidget(self.caucionesTable)

        self.nuevaCaucionBtn = QPushButton(caucionesWidget)
        self.nuevaCaucionBtn.setObjectName(u"nuevaCaucionBtn")
        self.nuevaCaucionBtn.setMinimumSize(QSize(782, 65))
        self.nuevaCaucionBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.nuevaCaucionBtn.setStyleSheet(u"background-color: \"green\";\n"
"color: \"white\";\n"
"margin: 10;")

        self.verticalLayout.addWidget(self.nuevaCaucionBtn)


        self.retranslateUi(caucionesWidget)

        QMetaObject.connectSlotsByName(caucionesWidget)
    # setupUi

    def retranslateUi(self, caucionesWidget):
        caucionesWidget.setWindowTitle(QCoreApplication.translate("caucionesWidget", u"Cauciones", None))
        self.nuevaCaucionBtn.setText(QCoreApplication.translate("caucionesWidget", u"Nueva cauci\u00f3n", None))
    # retranslateUi

