# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nuevaCaucionDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_nuevaCaucionDlg(object):
    def setupUi(self, nuevaCaucionDlg):
        if not nuevaCaucionDlg.objectName():
            nuevaCaucionDlg.setObjectName(u"nuevaCaucionDlg")
        nuevaCaucionDlg.resize(897, 592)
        nuevaCaucionDlg.setStyleSheet(u"background: \"black\"; color: \"white\"")
        self.verticalLayout = QVBoxLayout(nuevaCaucionDlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(nuevaCaucionDlg)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(101, 16))

        self.horizontalLayout_5.addWidget(self.label)

        self.currentDateInput = QDateEdit(nuevaCaucionDlg)
        self.currentDateInput.setObjectName(u"currentDateInput")
        self.currentDateInput.setMinimumSize(QSize(191, 22))
        self.currentDateInput.setCalendarPopup(True)
        self.currentDateInput.setDate(QDate(2024, 11, 20))

        self.horizontalLayout_5.addWidget(self.currentDateInput)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_4 = QLabel(nuevaCaucionDlg)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(101, 16))

        self.horizontalLayout_11.addWidget(self.label_4)

        self.montoInput = QDoubleSpinBox(nuevaCaucionDlg)
        self.montoInput.setObjectName(u"montoInput")
        self.montoInput.setEnabled(True)
        self.montoInput.setMinimumSize(QSize(191, 0))
        self.montoInput.setMinimum(0.000000000000000)
        self.montoInput.setMaximum(100000000000000000.000000000000000)
        self.montoInput.setValue(0.000000000000000)

        self.horizontalLayout_11.addWidget(self.montoInput)


        self.gridLayout_2.addLayout(self.horizontalLayout_11, 0, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(nuevaCaucionDlg)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(101, 16))

        self.horizontalLayout_6.addWidget(self.label_2)

        self.tnaInput = QDoubleSpinBox(nuevaCaucionDlg)
        self.tnaInput.setObjectName(u"tnaInput")
        self.tnaInput.setMinimumSize(QSize(191, 0))
        self.tnaInput.setMaximum(100.000000000000000)

        self.horizontalLayout_6.addWidget(self.tnaInput)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(nuevaCaucionDlg)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(101, 16))

        self.horizontalLayout_7.addWidget(self.label_7)

        self.comisionInput = QDoubleSpinBox(nuevaCaucionDlg)
        self.comisionInput.setObjectName(u"comisionInput")
        self.comisionInput.setMinimumSize(QSize(191, 0))
        self.comisionInput.setMaximum(100.000000000000000)

        self.horizontalLayout_7.addWidget(self.comisionInput)


        self.gridLayout_2.addLayout(self.horizontalLayout_7, 1, 1, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_3 = QLabel(nuevaCaucionDlg)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(101, 16))

        self.horizontalLayout_10.addWidget(self.label_3)

        self.daysInput = QSpinBox(nuevaCaucionDlg)
        self.daysInput.setObjectName(u"daysInput")
        self.daysInput.setMinimumSize(QSize(191, 0))
        self.daysInput.setMaximum(365)

        self.horizontalLayout_10.addWidget(self.daysInput)


        self.gridLayout_2.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(nuevaCaucionDlg)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(101, 16))

        self.horizontalLayout_8.addWidget(self.label_8)

        self.derechoMercadoInput = QDoubleSpinBox(nuevaCaucionDlg)
        self.derechoMercadoInput.setObjectName(u"derechoMercadoInput")
        self.derechoMercadoInput.setMinimumSize(QSize(191, 0))
        self.derechoMercadoInput.setDecimals(3)
        self.derechoMercadoInput.setMaximum(100.000000000000000)

        self.horizontalLayout_8.addWidget(self.derechoMercadoInput)


        self.gridLayout_2.addLayout(self.horizontalLayout_8, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.frame = QFrame(nuevaCaucionDlg)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: \"green\";\n"
"color: \"white\";\n"
"border-radius: 10")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 41))
        self.label_5.setMaximumSize(QSize(16777215, 41))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        self.montoTotalLbl = QLabel(self.frame)
        self.montoTotalLbl.setObjectName(u"montoTotalLbl")
        font1 = QFont()
        font1.setFamilies([u"Rockwell"])
        font1.setPointSize(20)
        font1.setBold(False)
        self.montoTotalLbl.setFont(font1)
        self.montoTotalLbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.montoTotalLbl)


        self.verticalLayout.addWidget(self.frame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(nuevaCaucionDlg)
        self.label_6.setObjectName(u"label_6")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(True)
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"background: rgb(204,107,0);\n"
"padding-left:5;\n"
"border-top-left-radius:10;\n"
"border-bottom-left-radius:10")

        self.horizontalLayout.addWidget(self.label_6)

        self.montoImporteBrutoLbl = QLabel(nuevaCaucionDlg)
        self.montoImporteBrutoLbl.setObjectName(u"montoImporteBrutoLbl")
        self.montoImporteBrutoLbl.setMinimumSize(QSize(0, 41))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setWeight(QFont.DemiBold)
        self.montoImporteBrutoLbl.setFont(font3)
        self.montoImporteBrutoLbl.setStyleSheet(u"background: rgb(204,107,0);\n"
"padding-left:5;\n"
"border-top-right-radius:10;\n"
"border-bottom-right-radius:10")

        self.horizontalLayout.addWidget(self.montoImporteBrutoLbl)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_11 = QLabel(nuevaCaucionDlg)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"background: rgb(204,107,0);\n"
"padding-left:5;\n"
"border-top-left-radius:10;\n"
"border-bottom-left-radius:10")

        self.horizontalLayout_3.addWidget(self.label_11)

        self.montoDerechoMercadoLbl = QLabel(nuevaCaucionDlg)
        self.montoDerechoMercadoLbl.setObjectName(u"montoDerechoMercadoLbl")
        self.montoDerechoMercadoLbl.setMinimumSize(QSize(0, 41))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setWeight(QFont.DemiBold)
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        font4.setKerning(True)
        self.montoDerechoMercadoLbl.setFont(font4)
        self.montoDerechoMercadoLbl.setStyleSheet(u"background: rgb(204,107,0);\n"
"padding-left:5;\n"
"border-top-right-radius:10;\n"
"border-bottom-right-radius:10")

        self.horizontalLayout_3.addWidget(self.montoDerechoMercadoLbl)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_10 = QLabel(nuevaCaucionDlg)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"background: rgb(204,107,0);\n"
"padding-left:5;\n"
"border-top-left-radius:10;\n"
"border-bottom-left-radius:10")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.montoComisionesLbl = QLabel(nuevaCaucionDlg)
        self.montoComisionesLbl.setObjectName(u"montoComisionesLbl")
        self.montoComisionesLbl.setMinimumSize(QSize(0, 41))
        self.montoComisionesLbl.setFont(font3)
        self.montoComisionesLbl.setStyleSheet(u"background: rgb(204,107,0);\n"
"padding-left:5;\n"
"border-top-right-radius:10;\n"
"border-bottom-right-radius:10")

        self.horizontalLayout_2.addWidget(self.montoComisionesLbl)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_12 = QLabel(nuevaCaucionDlg)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"background: rgb(204,107,0);\n"
"padding-left:5;\n"
"border-bottom-left-radius:10;\n"
"border-top-left-radius:10")

        self.horizontalLayout_4.addWidget(self.label_12)

        self.montoIVALbl = QLabel(nuevaCaucionDlg)
        self.montoIVALbl.setObjectName(u"montoIVALbl")
        self.montoIVALbl.setMinimumSize(QSize(0, 41))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setWeight(QFont.DemiBold)
        self.montoIVALbl.setFont(font5)
        self.montoIVALbl.setStyleSheet(u"background: rgb(204,107,0);\n"
"padding-left:5;\n"
"border-bottom-right-radius:10;\n"
"border-top-right-radius:10")

        self.horizontalLayout_4.addWidget(self.montoIVALbl)


        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_2 = QFrame(nuevaCaucionDlg)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(421, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 131))
        self.frame_2.setStyleSheet(u"background-color: \"green\";\n"
"color: \"white\";\n"
"border-radius: 10")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 41))
        self.label_13.setMaximumSize(QSize(16777215, 41))
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_13)

        self.gananciaNetaLbl = QLabel(self.frame_2)
        self.gananciaNetaLbl.setObjectName(u"gananciaNetaLbl")
        self.gananciaNetaLbl.setFont(font1)
        self.gananciaNetaLbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.gananciaNetaLbl)


        self.horizontalLayout_14.addWidget(self.frame_2)

        self.frame_3 = QFrame(nuevaCaucionDlg)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(421, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 101))
        self.frame_3.setStyleSheet(u"background-color: \"green\";\n"
"color: \"white\";\n"
"border-radius: 10")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 41))
        self.label_14.setMaximumSize(QSize(16777215, 41))
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_14)

        self.fechaLiquidacionLbl = QLabel(self.frame_3)
        self.fechaLiquidacionLbl.setObjectName(u"fechaLiquidacionLbl")
        self.fechaLiquidacionLbl.setFont(font1)
        self.fechaLiquidacionLbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.fechaLiquidacionLbl)


        self.horizontalLayout_14.addWidget(self.frame_3)


        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.widget = QWidget(nuevaCaucionDlg)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(851, 40))
        self.widget.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_13 = QHBoxLayout(self.widget)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer = QSpacerItem(696, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)

        self.saveBtn = QPushButton(self.widget)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setStyleSheet(u"background: \"green\"; color: \"white\"")

        self.horizontalLayout_13.addWidget(self.saveBtn)

        self.cancelBtn = QPushButton(self.widget)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout_13.addWidget(self.cancelBtn)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(nuevaCaucionDlg)

        QMetaObject.connectSlotsByName(nuevaCaucionDlg)
    # setupUi

    def retranslateUi(self, nuevaCaucionDlg):
        nuevaCaucionDlg.setWindowTitle(QCoreApplication.translate("nuevaCaucionDlg", u"Nueva Cauci\u00f3n", None))
        self.label.setText(QCoreApplication.translate("nuevaCaucionDlg", u"Fecha", None))
        self.label_4.setText(QCoreApplication.translate("nuevaCaucionDlg", u"Monto", None))
        self.label_2.setText(QCoreApplication.translate("nuevaCaucionDlg", u"TNA %", None))
        self.label_7.setText(QCoreApplication.translate("nuevaCaucionDlg", u"Comision %", None))
        self.label_3.setText(QCoreApplication.translate("nuevaCaucionDlg", u"Cantidad de d\u00edas", None))
        self.label_8.setText(QCoreApplication.translate("nuevaCaucionDlg", u"Derecho de mercado %", None))
        self.label_5.setText(QCoreApplication.translate("nuevaCaucionDlg", u"MONTO TOTAL", None))
        self.montoTotalLbl.setText(QCoreApplication.translate("nuevaCaucionDlg", u"$0,00", None))
        self.label_6.setText(QCoreApplication.translate("nuevaCaucionDlg", u"Importe Bruto", None))
        self.montoImporteBrutoLbl.setText(QCoreApplication.translate("nuevaCaucionDlg", u"$0,00", None))
        self.label_11.setText(QCoreApplication.translate("nuevaCaucionDlg", u"Derecho de mercado", None))
        self.montoDerechoMercadoLbl.setText(QCoreApplication.translate("nuevaCaucionDlg", u"$0,00", None))
        self.label_10.setText(QCoreApplication.translate("nuevaCaucionDlg", u"Comisi\u00f3n", None))
        self.montoComisionesLbl.setText(QCoreApplication.translate("nuevaCaucionDlg", u"$0,00", None))
        self.label_12.setText(QCoreApplication.translate("nuevaCaucionDlg", u"IVA 21%", None))
        self.montoIVALbl.setText(QCoreApplication.translate("nuevaCaucionDlg", u"$0,00", None))
        self.label_13.setText(QCoreApplication.translate("nuevaCaucionDlg", u"GANANCIA NETA", None))
        self.gananciaNetaLbl.setText(QCoreApplication.translate("nuevaCaucionDlg", u"$0,00", None))
        self.label_14.setText(QCoreApplication.translate("nuevaCaucionDlg", u"FECHA DE LIQUIDACI\u00d3N", None))
        self.fechaLiquidacionLbl.setText(QCoreApplication.translate("nuevaCaucionDlg", u"23/11/2024", None))
        self.saveBtn.setText(QCoreApplication.translate("nuevaCaucionDlg", u"Guardar", None))
        self.cancelBtn.setText(QCoreApplication.translate("nuevaCaucionDlg", u"Cancelar", None))
    # retranslateUi

