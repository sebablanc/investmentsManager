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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1080, 730)
        Form.setStyleSheet(u"background-color: \"black\";\n"
"color: \"white\";")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.caucionesTable = QTableView(Form)
        self.caucionesTable.setObjectName(u"caucionesTable")
        self.caucionesTable.setStyleSheet(u"background: \"lightgray\"; color: \"black\"")

        self.verticalLayout.addWidget(self.caucionesTable)

        self.nuevaCaucionBtn = QPushButton(Form)
        self.nuevaCaucionBtn.setObjectName(u"nuevaCaucionBtn")
        self.nuevaCaucionBtn.setMinimumSize(QSize(782, 65))
        self.nuevaCaucionBtn.setStyleSheet(u"background-color: \"green\";\n"
"color: \"white\";\n"
"margin: 10;")

        self.verticalLayout.addWidget(self.nuevaCaucionBtn)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.nuevaCaucionBtn.setText(QCoreApplication.translate("Form", u"Nueva cauci\u00f3n", None))
    # retranslateUi

