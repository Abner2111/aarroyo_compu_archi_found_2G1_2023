# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProcesadoresGUIWMBcHS.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_seleccionProceWindow(object):
    def setupUi(self, seleccionProceWindow):
        if not seleccionProceWindow.objectName():
            seleccionProceWindow.setObjectName(u"seleccionProceWindow")
        seleccionProceWindow.resize(830, 594)
        seleccionProceWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(seleccionProceWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(140, 60, 521, 421))
        font = QFont()
        font.setPointSize(12)
        self.gridLayoutWidget_2.setFont(font)
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.multicicloButton = QPushButton(self.gridLayoutWidget_2)
        self.multicicloButton.setObjectName(u"multicicloButton")
        self.multicicloButton.setFont(font)
        self.multicicloButton.setIconSize(QSize(16, 16))
        self.multicicloButton.setFlat(False)

        self.gridLayout_2.addWidget(self.multicicloButton, 1, 0, 1, 1)

        self.unicicloButton = QPushButton(self.gridLayoutWidget_2)
        self.unicicloButton.setObjectName(u"unicicloButton")
        self.unicicloButton.setFont(font)
        self.unicicloButton.setIconSize(QSize(16, 16))
        self.unicicloButton.setFlat(False)

        self.gridLayout_2.addWidget(self.unicicloButton, 0, 0, 1, 1)

        self.segmentadoStallsButton = QPushButton(self.gridLayoutWidget_2)
        self.segmentadoStallsButton.setObjectName(u"segmentadoStallsButton")
        self.segmentadoStallsButton.setFont(font)
        self.segmentadoStallsButton.setIconSize(QSize(16, 16))
        self.segmentadoStallsButton.setFlat(False)

        self.gridLayout_2.addWidget(self.segmentadoStallsButton, 3, 0, 1, 1)

        self.segmentadoForwardingButton = QPushButton(self.gridLayoutWidget_2)
        self.segmentadoForwardingButton.setObjectName(u"segmentadoForwardingButton")
        self.segmentadoForwardingButton.setFont(font)
        self.segmentadoForwardingButton.setIconSize(QSize(16, 16))
        self.segmentadoForwardingButton.setFlat(False)

        self.gridLayout_2.addWidget(self.segmentadoForwardingButton, 2, 0, 1, 1)

        self.seleccionProceLabel = QLabel(self.centralwidget)
        self.seleccionProceLabel.setObjectName(u"seleccionProceLabel")
        self.seleccionProceLabel.setGeometry(QRect(20, 10, 371, 31))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setStrikeOut(False)
        self.seleccionProceLabel.setFont(font1)
        self.estadisticasButton = QPushButton(self.centralwidget)
        self.estadisticasButton.setObjectName(u"estadisticasButton")
        self.estadisticasButton.setGeometry(QRect(650, 510, 121, 41))
        self.estadisticasButton.setFont(font)
        seleccionProceWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(seleccionProceWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 830, 22))
        seleccionProceWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(seleccionProceWindow)
        self.statusbar.setObjectName(u"statusbar")
        seleccionProceWindow.setStatusBar(self.statusbar)

        self.retranslateUi(seleccionProceWindow)

        self.multicicloButton.setDefault(True)
        self.unicicloButton.setDefault(True)
        self.segmentadoStallsButton.setDefault(True)
        self.segmentadoForwardingButton.setDefault(True)


        QMetaObject.connectSlotsByName(seleccionProceWindow)
    # setupUi

    def retranslateUi(self, seleccionProceWindow):
        seleccionProceWindow.setWindowTitle(QCoreApplication.translate("seleccionProceWindow", u"Procesadores", None))
        self.multicicloButton.setText(QCoreApplication.translate("seleccionProceWindow", u"MULTICICLO", None))
        self.unicicloButton.setText(QCoreApplication.translate("seleccionProceWindow", u"UNICICLO", None))
        self.segmentadoStallsButton.setText(QCoreApplication.translate("seleccionProceWindow", u"SEGMENTADO CON STALLS", None))
        self.segmentadoForwardingButton.setText(QCoreApplication.translate("seleccionProceWindow", u"SEGMENTADO CON FORWARDING", None))
        self.seleccionProceLabel.setText(QCoreApplication.translate("seleccionProceWindow", u"Seleccione el procesador que desea", None))
        self.estadisticasButton.setText(QCoreApplication.translate("seleccionProceWindow", u"Estadisticas", None))
    # retranslateUi

