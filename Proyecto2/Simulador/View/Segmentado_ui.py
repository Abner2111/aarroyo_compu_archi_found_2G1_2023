# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SegmentadoGUIyDtkxT.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLCDNumber, QLabel,
    QMainWindow, QMenuBar, QScrollArea, QSizePolicy,
    QStatusBar, QWidget)

class Ui_SegmentadoWindow(object):
    def setupUi(self, SegmentadoWindow):
        if not SegmentadoWindow.objectName():
            SegmentadoWindow.setObjectName(u"SegmentadoWindow")
        SegmentadoWindow.resize(811, 626)
        self.centralwidget = QWidget(SegmentadoWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 141, 71))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        font.setBold(True)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setAutoFillBackground(False)
        self.pcLabel = QLabel(self.centralwidget)
        self.pcLabel.setObjectName(u"pcLabel")
        self.pcLabel.setGeometry(QRect(10, 110, 81, 31))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.pcLabel.setFont(font1)
        self.pcNumberLabel = QLabel(self.centralwidget)
        self.pcNumberLabel.setObjectName(u"pcNumberLabel")
        self.pcNumberLabel.setGeometry(QRect(10, 150, 71, 41))
        font2 = QFont()
        font2.setPointSize(11)
        self.pcNumberLabel.setFont(font2)
        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(10, 70, 71, 23))
        self.registroArea = QScrollArea(self.centralwidget)
        self.registroArea.setObjectName(u"registroArea")
        self.registroArea.setGeometry(QRect(30, 230, 161, 331))
        self.registroArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 142, 742))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName(u"formLayout")
        self.rxMainLabel = QLabel(self.scrollAreaWidgetContents)
        self.rxMainLabel.setObjectName(u"rxMainLabel")
        self.rxMainLabel.setFont(font2)
        self.rxMainLabel.setTextFormat(Qt.AutoText)
        self.rxMainLabel.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.rxMainLabel)

        self.valueRegistrosMainLabel = QLabel(self.scrollAreaWidgetContents)
        self.valueRegistrosMainLabel.setObjectName(u"valueRegistrosMainLabel")
        self.valueRegistrosMainLabel.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.valueRegistrosMainLabel)

        self.rxLabel2 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel2.setObjectName(u"rxLabel2")
        font3 = QFont()
        font3.setPointSize(9)
        self.rxLabel2.setFont(font3)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.rxLabel2)

        self.valueMemLabel = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel.setObjectName(u"valueMemLabel")
        self.valueMemLabel.setFont(font3)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.valueMemLabel)

        self.rxLabel3 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel3.setObjectName(u"rxLabel3")
        self.rxLabel3.setFont(font3)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.rxLabel3)

        self.valueMemLabel_2 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_2.setObjectName(u"valueMemLabel_2")
        self.valueMemLabel_2.setFont(font3)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.valueMemLabel_2)

        self.rxLabel4 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel4.setObjectName(u"rxLabel4")
        self.rxLabel4.setFont(font3)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.rxLabel4)

        self.valueMemLabel_3 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_3.setObjectName(u"valueMemLabel_3")
        self.valueMemLabel_3.setFont(font3)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.valueMemLabel_3)

        self.rxLabel5 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel5.setObjectName(u"rxLabel5")
        self.rxLabel5.setFont(font3)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.rxLabel5)

        self.valueMemLabel_4 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_4.setObjectName(u"valueMemLabel_4")
        self.valueMemLabel_4.setFont(font3)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.valueMemLabel_4)

        self.rxLabel6 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel6.setObjectName(u"rxLabel6")
        self.rxLabel6.setFont(font3)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.rxLabel6)

        self.valueMemLabel_5 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_5.setObjectName(u"valueMemLabel_5")
        self.valueMemLabel_5.setFont(font3)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.valueMemLabel_5)

        self.valueMemLabel_10 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_10.setObjectName(u"valueMemLabel_10")
        self.valueMemLabel_10.setFont(font3)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.valueMemLabel_10)

        self.valueMemLabel_9 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_9.setObjectName(u"valueMemLabel_9")
        self.valueMemLabel_9.setFont(font3)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.valueMemLabel_9)

        self.valueMemLabel_8 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_8.setObjectName(u"valueMemLabel_8")
        self.valueMemLabel_8.setFont(font3)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.valueMemLabel_8)

        self.valueMemLabel_7 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_7.setObjectName(u"valueMemLabel_7")
        self.valueMemLabel_7.setFont(font3)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.valueMemLabel_7)

        self.valueMemLabel_6 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_6.setObjectName(u"valueMemLabel_6")
        self.valueMemLabel_6.setFont(font3)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.valueMemLabel_6)

        self.rxLabel7 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel7.setObjectName(u"rxLabel7")
        self.rxLabel7.setFont(font3)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.rxLabel7)

        self.rxLabel8 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel8.setObjectName(u"rxLabel8")
        self.rxLabel8.setFont(font3)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.rxLabel8)

        self.rxLabel9 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel9.setObjectName(u"rxLabel9")
        self.rxLabel9.setFont(font3)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.rxLabel9)

        self.rxLabel10 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel10.setObjectName(u"rxLabel10")
        self.rxLabel10.setFont(font3)

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.rxLabel10)

        self.rxLabel11 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel11.setObjectName(u"rxLabel11")
        self.rxLabel11.setFont(font3)

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.rxLabel11)

        self.rxLabel12 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel12.setObjectName(u"rxLabel12")
        self.rxLabel12.setFont(font3)

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.rxLabel12)

        self.valueMemLabel_11 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_11.setObjectName(u"valueMemLabel_11")
        self.valueMemLabel_11.setFont(font3)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.valueMemLabel_11)

        self.rxLabel13 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel13.setObjectName(u"rxLabel13")
        self.rxLabel13.setFont(font3)

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.rxLabel13)

        self.valueMemLabel_12 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_12.setObjectName(u"valueMemLabel_12")
        self.valueMemLabel_12.setFont(font3)

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.valueMemLabel_12)

        self.valueMemLabel_22 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_22.setObjectName(u"valueMemLabel_22")
        self.valueMemLabel_22.setFont(font3)

        self.formLayout.setWidget(22, QFormLayout.FieldRole, self.valueMemLabel_22)

        self.valueMemLabel_21 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_21.setObjectName(u"valueMemLabel_21")
        self.valueMemLabel_21.setFont(font3)

        self.formLayout.setWidget(21, QFormLayout.FieldRole, self.valueMemLabel_21)

        self.valueMemLabel_20 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_20.setObjectName(u"valueMemLabel_20")
        self.valueMemLabel_20.setFont(font3)

        self.formLayout.setWidget(20, QFormLayout.FieldRole, self.valueMemLabel_20)

        self.valueMemLabel_19 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_19.setObjectName(u"valueMemLabel_19")
        self.valueMemLabel_19.setFont(font3)

        self.formLayout.setWidget(19, QFormLayout.FieldRole, self.valueMemLabel_19)

        self.valueMemLabel_18 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_18.setObjectName(u"valueMemLabel_18")
        self.valueMemLabel_18.setFont(font3)

        self.formLayout.setWidget(18, QFormLayout.FieldRole, self.valueMemLabel_18)

        self.valueMemLabel_17 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_17.setObjectName(u"valueMemLabel_17")
        self.valueMemLabel_17.setFont(font3)

        self.formLayout.setWidget(17, QFormLayout.FieldRole, self.valueMemLabel_17)

        self.valueMemLabel_16 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_16.setObjectName(u"valueMemLabel_16")
        self.valueMemLabel_16.setFont(font3)

        self.formLayout.setWidget(16, QFormLayout.FieldRole, self.valueMemLabel_16)

        self.valueMemLabel_15 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_15.setObjectName(u"valueMemLabel_15")
        self.valueMemLabel_15.setFont(font3)

        self.formLayout.setWidget(15, QFormLayout.FieldRole, self.valueMemLabel_15)

        self.valueMemLabel_14 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_14.setObjectName(u"valueMemLabel_14")
        self.valueMemLabel_14.setFont(font3)

        self.formLayout.setWidget(14, QFormLayout.FieldRole, self.valueMemLabel_14)

        self.valueMemLabel_13 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_13.setObjectName(u"valueMemLabel_13")
        self.valueMemLabel_13.setFont(font3)

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.valueMemLabel_13)

        self.rxLabel14 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel14.setObjectName(u"rxLabel14")
        self.rxLabel14.setFont(font3)

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.rxLabel14)

        self.rxLabel15 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel15.setObjectName(u"rxLabel15")
        self.rxLabel15.setFont(font3)

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.rxLabel15)

        self.rxLabel16 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel16.setObjectName(u"rxLabel16")
        self.rxLabel16.setFont(font3)

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.rxLabel16)

        self.rxLabel17 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel17.setObjectName(u"rxLabel17")
        self.rxLabel17.setFont(font3)

        self.formLayout.setWidget(16, QFormLayout.LabelRole, self.rxLabel17)

        self.rxLabel18 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel18.setObjectName(u"rxLabel18")
        self.rxLabel18.setFont(font3)

        self.formLayout.setWidget(17, QFormLayout.LabelRole, self.rxLabel18)

        self.rxLabel19 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel19.setObjectName(u"rxLabel19")
        self.rxLabel19.setFont(font3)

        self.formLayout.setWidget(18, QFormLayout.LabelRole, self.rxLabel19)

        self.rxLabel20 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel20.setObjectName(u"rxLabel20")
        self.rxLabel20.setFont(font3)

        self.formLayout.setWidget(19, QFormLayout.LabelRole, self.rxLabel20)

        self.rxLabel21 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel21.setObjectName(u"rxLabel21")
        self.rxLabel21.setFont(font3)

        self.formLayout.setWidget(20, QFormLayout.LabelRole, self.rxLabel21)

        self.rxLabel22 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel22.setObjectName(u"rxLabel22")
        self.rxLabel22.setFont(font3)

        self.formLayout.setWidget(21, QFormLayout.LabelRole, self.rxLabel22)

        self.rxLabel23 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel23.setObjectName(u"rxLabel23")
        self.rxLabel23.setFont(font3)

        self.formLayout.setWidget(22, QFormLayout.LabelRole, self.rxLabel23)

        self.rxLabel24 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel24.setObjectName(u"rxLabel24")
        self.rxLabel24.setFont(font3)

        self.formLayout.setWidget(23, QFormLayout.LabelRole, self.rxLabel24)

        self.valueMemLabel_23 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_23.setObjectName(u"valueMemLabel_23")
        self.valueMemLabel_23.setFont(font3)

        self.formLayout.setWidget(23, QFormLayout.FieldRole, self.valueMemLabel_23)

        self.rxLabel25 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel25.setObjectName(u"rxLabel25")
        self.rxLabel25.setFont(font3)

        self.formLayout.setWidget(24, QFormLayout.LabelRole, self.rxLabel25)

        self.rxLabel30 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel30.setObjectName(u"rxLabel30")
        self.rxLabel30.setFont(font3)

        self.formLayout.setWidget(29, QFormLayout.LabelRole, self.rxLabel30)

        self.rxLabel29 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel29.setObjectName(u"rxLabel29")
        self.rxLabel29.setFont(font3)

        self.formLayout.setWidget(28, QFormLayout.LabelRole, self.rxLabel29)

        self.rxLabel28 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel28.setObjectName(u"rxLabel28")
        self.rxLabel28.setFont(font3)

        self.formLayout.setWidget(27, QFormLayout.LabelRole, self.rxLabel28)

        self.rxLabel27 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel27.setObjectName(u"rxLabel27")
        self.rxLabel27.setFont(font3)

        self.formLayout.setWidget(26, QFormLayout.LabelRole, self.rxLabel27)

        self.rxLabel26 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel26.setObjectName(u"rxLabel26")
        self.rxLabel26.setFont(font3)

        self.formLayout.setWidget(25, QFormLayout.LabelRole, self.rxLabel26)

        self.valueMemLabel_24 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_24.setObjectName(u"valueMemLabel_24")
        self.valueMemLabel_24.setFont(font3)

        self.formLayout.setWidget(24, QFormLayout.FieldRole, self.valueMemLabel_24)

        self.valueMemLabel_25 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_25.setObjectName(u"valueMemLabel_25")
        self.valueMemLabel_25.setFont(font3)

        self.formLayout.setWidget(25, QFormLayout.FieldRole, self.valueMemLabel_25)

        self.valueMemLabel_26 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_26.setObjectName(u"valueMemLabel_26")
        self.valueMemLabel_26.setFont(font3)

        self.formLayout.setWidget(26, QFormLayout.FieldRole, self.valueMemLabel_26)

        self.valueMemLabel_27 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_27.setObjectName(u"valueMemLabel_27")
        self.valueMemLabel_27.setFont(font3)

        self.formLayout.setWidget(27, QFormLayout.FieldRole, self.valueMemLabel_27)

        self.valueMemLabel_28 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_28.setObjectName(u"valueMemLabel_28")
        self.valueMemLabel_28.setFont(font3)

        self.formLayout.setWidget(28, QFormLayout.FieldRole, self.valueMemLabel_28)

        self.valueMemLabel_29 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_29.setObjectName(u"valueMemLabel_29")
        self.valueMemLabel_29.setFont(font3)

        self.formLayout.setWidget(29, QFormLayout.FieldRole, self.valueMemLabel_29)

        self.valueMemLabel_30 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_30.setObjectName(u"valueMemLabel_30")
        self.valueMemLabel_30.setFont(font3)

        self.formLayout.setWidget(30, QFormLayout.FieldRole, self.valueMemLabel_30)

        self.valueMemLabel_31 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_31.setObjectName(u"valueMemLabel_31")
        self.valueMemLabel_31.setFont(font3)

        self.formLayout.setWidget(31, QFormLayout.FieldRole, self.valueMemLabel_31)

        self.rxLabel31 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel31.setObjectName(u"rxLabel31")
        self.rxLabel31.setFont(font3)

        self.formLayout.setWidget(30, QFormLayout.LabelRole, self.rxLabel31)

        self.rxLabel32 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel32.setObjectName(u"rxLabel32")
        self.rxLabel32.setFont(font3)

        self.formLayout.setWidget(31, QFormLayout.LabelRole, self.rxLabel32)

        self.rxLabel33 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel33.setObjectName(u"rxLabel33")
        self.rxLabel33.setFont(font3)

        self.formLayout.setWidget(32, QFormLayout.LabelRole, self.rxLabel33)

        self.valueMemLabel_32 = QLabel(self.scrollAreaWidgetContents)
        self.valueMemLabel_32.setObjectName(u"valueMemLabel_32")
        self.valueMemLabel_32.setFont(font3)

        self.formLayout.setWidget(32, QFormLayout.FieldRole, self.valueMemLabel_32)

        self.registroArea.setWidget(self.scrollAreaWidgetContents)
        self.registroMainLabel = QLabel(self.centralwidget)
        self.registroMainLabel.setObjectName(u"registroMainLabel")
        self.registroMainLabel.setGeometry(QRect(70, 180, 71, 31))
        font4 = QFont()
        font4.setPointSize(12)
        self.registroMainLabel.setFont(font4)
        self.memoriaArea = QScrollArea(self.centralwidget)
        self.memoriaArea.setObjectName(u"memoriaArea")
        self.memoriaArea.setGeometry(QRect(790, 570, 161, 331))
        self.memoriaArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 142, 1798))
        self.formLayout_2 = QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.rxMainLabel_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.rxMainLabel_3.setObjectName(u"rxMainLabel_3")
        self.rxMainLabel_3.setFont(font2)
        self.rxMainLabel_3.setTextFormat(Qt.AutoText)
        self.rxMainLabel_3.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.rxMainLabel_3)

        self.valueRegistrosLabel_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueRegistrosLabel_3.setObjectName(u"valueRegistrosLabel_3")
        self.valueRegistrosLabel_3.setFont(font2)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.valueRegistrosLabel_3)

        self.addrLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel.setObjectName(u"addrLabel")
        self.addrLabel.setFont(font3)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.addrLabel)

        self.valueLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel.setObjectName(u"valueLabel")
        self.valueLabel.setFont(font3)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.valueLabel)

        self.addrLabel_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_2.setObjectName(u"addrLabel_2")
        self.addrLabel_2.setFont(font3)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.addrLabel_2)

        self.valueLabel_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_2.setObjectName(u"valueLabel_2")
        self.valueLabel_2.setFont(font3)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.valueLabel_2)

        self.addrLabel_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_3.setObjectName(u"addrLabel_3")
        self.addrLabel_3.setFont(font3)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.addrLabel_3)

        self.valueLabel_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_3.setObjectName(u"valueLabel_3")
        self.valueLabel_3.setFont(font3)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.valueLabel_3)

        self.addrLabel_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_4.setObjectName(u"addrLabel_4")
        self.addrLabel_4.setFont(font3)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.addrLabel_4)

        self.valueLabel_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_4.setObjectName(u"valueLabel_4")
        self.valueLabel_4.setFont(font3)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.valueLabel_4)

        self.addrLabel_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_5.setObjectName(u"addrLabel_5")
        self.addrLabel_5.setFont(font3)

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.addrLabel_5)

        self.valueLabel_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_5.setObjectName(u"valueLabel_5")
        self.valueLabel_5.setFont(font3)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.valueLabel_5)

        self.addrLabel_6 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_6.setObjectName(u"addrLabel_6")
        self.addrLabel_6.setFont(font3)

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.addrLabel_6)

        self.valueLabel_6 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_6.setObjectName(u"valueLabel_6")
        self.valueLabel_6.setFont(font3)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.valueLabel_6)

        self.addrLabel_7 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_7.setObjectName(u"addrLabel_7")
        self.addrLabel_7.setFont(font3)

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.addrLabel_7)

        self.valueLabel_7 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_7.setObjectName(u"valueLabel_7")
        self.valueLabel_7.setFont(font3)

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.valueLabel_7)

        self.addrLabel_8 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_8.setObjectName(u"addrLabel_8")
        self.addrLabel_8.setFont(font3)

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.addrLabel_8)

        self.valueLabel_8 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_8.setObjectName(u"valueLabel_8")
        self.valueLabel_8.setFont(font3)

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.valueLabel_8)

        self.addrLabel_9 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_9.setObjectName(u"addrLabel_9")
        self.addrLabel_9.setFont(font3)

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.addrLabel_9)

        self.valueLabel_9 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_9.setObjectName(u"valueLabel_9")
        self.valueLabel_9.setFont(font3)

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.valueLabel_9)

        self.addrLabel_10 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_10.setObjectName(u"addrLabel_10")
        self.addrLabel_10.setFont(font3)

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.addrLabel_10)

        self.valueLabel_10 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_10.setObjectName(u"valueLabel_10")
        self.valueLabel_10.setFont(font3)

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.valueLabel_10)

        self.addrLabel_16 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_16.setObjectName(u"addrLabel_16")
        self.addrLabel_16.setFont(font3)

        self.formLayout_2.setWidget(11, QFormLayout.LabelRole, self.addrLabel_16)

        self.valueLabel_11 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_11.setObjectName(u"valueLabel_11")
        self.valueLabel_11.setFont(font3)

        self.formLayout_2.setWidget(11, QFormLayout.FieldRole, self.valueLabel_11)

        self.addrLabel_18 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_18.setObjectName(u"addrLabel_18")
        self.addrLabel_18.setFont(font3)

        self.formLayout_2.setWidget(12, QFormLayout.LabelRole, self.addrLabel_18)

        self.valueLabel_12 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_12.setObjectName(u"valueLabel_12")
        self.valueLabel_12.setFont(font3)

        self.formLayout_2.setWidget(12, QFormLayout.FieldRole, self.valueLabel_12)

        self.addrLabel_14 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_14.setObjectName(u"addrLabel_14")
        self.addrLabel_14.setFont(font3)

        self.formLayout_2.setWidget(13, QFormLayout.LabelRole, self.addrLabel_14)

        self.valueLabel_13 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_13.setObjectName(u"valueLabel_13")
        self.valueLabel_13.setFont(font3)

        self.formLayout_2.setWidget(13, QFormLayout.FieldRole, self.valueLabel_13)

        self.addrLabel_12 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_12.setObjectName(u"addrLabel_12")
        self.addrLabel_12.setFont(font3)

        self.formLayout_2.setWidget(14, QFormLayout.LabelRole, self.addrLabel_12)

        self.valueLabel_14 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_14.setObjectName(u"valueLabel_14")
        self.valueLabel_14.setFont(font3)

        self.formLayout_2.setWidget(14, QFormLayout.FieldRole, self.valueLabel_14)

        self.addrLabel_11 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_11.setObjectName(u"addrLabel_11")
        self.addrLabel_11.setFont(font3)

        self.formLayout_2.setWidget(15, QFormLayout.LabelRole, self.addrLabel_11)

        self.valueLabel_15 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_15.setObjectName(u"valueLabel_15")
        self.valueLabel_15.setFont(font3)

        self.formLayout_2.setWidget(15, QFormLayout.FieldRole, self.valueLabel_15)

        self.addrLabel_15 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_15.setObjectName(u"addrLabel_15")
        self.addrLabel_15.setFont(font3)

        self.formLayout_2.setWidget(16, QFormLayout.LabelRole, self.addrLabel_15)

        self.valueLabel_16 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_16.setObjectName(u"valueLabel_16")
        self.valueLabel_16.setFont(font3)

        self.formLayout_2.setWidget(16, QFormLayout.FieldRole, self.valueLabel_16)

        self.addrLabel_17 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_17.setObjectName(u"addrLabel_17")
        self.addrLabel_17.setFont(font3)

        self.formLayout_2.setWidget(17, QFormLayout.LabelRole, self.addrLabel_17)

        self.valueLabel_17 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_17.setObjectName(u"valueLabel_17")
        self.valueLabel_17.setFont(font3)

        self.formLayout_2.setWidget(17, QFormLayout.FieldRole, self.valueLabel_17)

        self.addrLabel_13 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_13.setObjectName(u"addrLabel_13")
        self.addrLabel_13.setFont(font3)

        self.formLayout_2.setWidget(18, QFormLayout.LabelRole, self.addrLabel_13)

        self.valueLabel_18 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_18.setObjectName(u"valueLabel_18")
        self.valueLabel_18.setFont(font3)

        self.formLayout_2.setWidget(18, QFormLayout.FieldRole, self.valueLabel_18)

        self.addrLabel_19 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_19.setObjectName(u"addrLabel_19")
        self.addrLabel_19.setFont(font3)

        self.formLayout_2.setWidget(19, QFormLayout.LabelRole, self.addrLabel_19)

        self.valueLabel_19 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_19.setObjectName(u"valueLabel_19")
        self.valueLabel_19.setFont(font3)

        self.formLayout_2.setWidget(19, QFormLayout.FieldRole, self.valueLabel_19)

        self.addrLabel_20 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_20.setObjectName(u"addrLabel_20")
        self.addrLabel_20.setFont(font3)

        self.formLayout_2.setWidget(20, QFormLayout.LabelRole, self.addrLabel_20)

        self.valueLabel_20 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_20.setObjectName(u"valueLabel_20")
        self.valueLabel_20.setFont(font3)

        self.formLayout_2.setWidget(20, QFormLayout.FieldRole, self.valueLabel_20)

        self.addrLabel_21 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_21.setObjectName(u"addrLabel_21")
        self.addrLabel_21.setFont(font3)

        self.formLayout_2.setWidget(21, QFormLayout.LabelRole, self.addrLabel_21)

        self.valueLabel_21 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_21.setObjectName(u"valueLabel_21")
        self.valueLabel_21.setFont(font3)

        self.formLayout_2.setWidget(21, QFormLayout.FieldRole, self.valueLabel_21)

        self.valueLabel_22 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_22.setObjectName(u"valueLabel_22")
        self.valueLabel_22.setFont(font3)

        self.formLayout_2.setWidget(22, QFormLayout.FieldRole, self.valueLabel_22)

        self.valueLabel_23 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_23.setObjectName(u"valueLabel_23")
        self.valueLabel_23.setFont(font3)

        self.formLayout_2.setWidget(23, QFormLayout.FieldRole, self.valueLabel_23)

        self.valueLabel_31 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_31.setObjectName(u"valueLabel_31")
        self.valueLabel_31.setFont(font3)

        self.formLayout_2.setWidget(31, QFormLayout.FieldRole, self.valueLabel_31)

        self.valueLabel_28 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_28.setObjectName(u"valueLabel_28")
        self.valueLabel_28.setFont(font3)

        self.formLayout_2.setWidget(30, QFormLayout.FieldRole, self.valueLabel_28)

        self.valueLabel_26 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_26.setObjectName(u"valueLabel_26")
        self.valueLabel_26.setFont(font3)

        self.formLayout_2.setWidget(29, QFormLayout.FieldRole, self.valueLabel_26)

        self.valueLabel_24 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_24.setObjectName(u"valueLabel_24")
        self.valueLabel_24.setFont(font3)

        self.formLayout_2.setWidget(28, QFormLayout.FieldRole, self.valueLabel_24)

        self.valueLabel_27 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_27.setObjectName(u"valueLabel_27")
        self.valueLabel_27.setFont(font3)

        self.formLayout_2.setWidget(27, QFormLayout.FieldRole, self.valueLabel_27)

        self.valueLabel_30 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_30.setObjectName(u"valueLabel_30")
        self.valueLabel_30.setFont(font3)

        self.formLayout_2.setWidget(26, QFormLayout.FieldRole, self.valueLabel_30)

        self.valueLabel_25 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_25.setObjectName(u"valueLabel_25")
        self.valueLabel_25.setFont(font3)

        self.formLayout_2.setWidget(25, QFormLayout.FieldRole, self.valueLabel_25)

        self.valueLabel_29 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_29.setObjectName(u"valueLabel_29")
        self.valueLabel_29.setFont(font3)

        self.formLayout_2.setWidget(24, QFormLayout.FieldRole, self.valueLabel_29)

        self.addrLabel_22 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_22.setObjectName(u"addrLabel_22")
        self.addrLabel_22.setFont(font3)

        self.formLayout_2.setWidget(22, QFormLayout.LabelRole, self.addrLabel_22)

        self.addrLabel_23 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_23.setObjectName(u"addrLabel_23")
        self.addrLabel_23.setFont(font3)

        self.formLayout_2.setWidget(23, QFormLayout.LabelRole, self.addrLabel_23)

        self.addrLabel_24 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_24.setObjectName(u"addrLabel_24")
        self.addrLabel_24.setFont(font3)

        self.formLayout_2.setWidget(24, QFormLayout.LabelRole, self.addrLabel_24)

        self.addrLabel_25 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_25.setObjectName(u"addrLabel_25")
        self.addrLabel_25.setFont(font3)

        self.formLayout_2.setWidget(25, QFormLayout.LabelRole, self.addrLabel_25)

        self.addrLabel_26 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_26.setObjectName(u"addrLabel_26")
        self.addrLabel_26.setFont(font3)

        self.formLayout_2.setWidget(26, QFormLayout.LabelRole, self.addrLabel_26)

        self.addrLabel_27 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_27.setObjectName(u"addrLabel_27")
        self.addrLabel_27.setFont(font3)

        self.formLayout_2.setWidget(27, QFormLayout.LabelRole, self.addrLabel_27)

        self.addrLabel_28 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_28.setObjectName(u"addrLabel_28")
        self.addrLabel_28.setFont(font3)

        self.formLayout_2.setWidget(28, QFormLayout.LabelRole, self.addrLabel_28)

        self.addrLabel_29 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_29.setObjectName(u"addrLabel_29")
        self.addrLabel_29.setFont(font3)

        self.formLayout_2.setWidget(29, QFormLayout.LabelRole, self.addrLabel_29)

        self.addrLabel_30 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_30.setObjectName(u"addrLabel_30")
        self.addrLabel_30.setFont(font3)

        self.formLayout_2.setWidget(30, QFormLayout.LabelRole, self.addrLabel_30)

        self.addrLabel_31 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_31.setObjectName(u"addrLabel_31")
        self.addrLabel_31.setFont(font3)

        self.formLayout_2.setWidget(31, QFormLayout.LabelRole, self.addrLabel_31)

        self.addrLabel_32 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_32.setObjectName(u"addrLabel_32")
        self.addrLabel_32.setFont(font3)

        self.formLayout_2.setWidget(32, QFormLayout.LabelRole, self.addrLabel_32)

        self.addrLabel_33 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_33.setObjectName(u"addrLabel_33")
        self.addrLabel_33.setFont(font3)

        self.formLayout_2.setWidget(33, QFormLayout.LabelRole, self.addrLabel_33)

        self.addrLabel_34 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_34.setObjectName(u"addrLabel_34")
        self.addrLabel_34.setFont(font3)

        self.formLayout_2.setWidget(34, QFormLayout.LabelRole, self.addrLabel_34)

        self.addrLabel_35 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_35.setObjectName(u"addrLabel_35")
        self.addrLabel_35.setFont(font3)

        self.formLayout_2.setWidget(35, QFormLayout.LabelRole, self.addrLabel_35)

        self.addrLabel_36 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_36.setObjectName(u"addrLabel_36")
        self.addrLabel_36.setFont(font3)

        self.formLayout_2.setWidget(36, QFormLayout.LabelRole, self.addrLabel_36)

        self.addrLabel_37 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_37.setObjectName(u"addrLabel_37")
        self.addrLabel_37.setFont(font3)

        self.formLayout_2.setWidget(37, QFormLayout.LabelRole, self.addrLabel_37)

        self.addrLabel_38 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_38.setObjectName(u"addrLabel_38")
        self.addrLabel_38.setFont(font3)

        self.formLayout_2.setWidget(38, QFormLayout.LabelRole, self.addrLabel_38)

        self.addrLabel_39 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_39.setObjectName(u"addrLabel_39")
        self.addrLabel_39.setFont(font3)

        self.formLayout_2.setWidget(39, QFormLayout.LabelRole, self.addrLabel_39)

        self.addrLabel_40 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_40.setObjectName(u"addrLabel_40")
        self.addrLabel_40.setFont(font3)

        self.formLayout_2.setWidget(40, QFormLayout.LabelRole, self.addrLabel_40)

        self.valueLabel_32 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_32.setObjectName(u"valueLabel_32")
        self.valueLabel_32.setFont(font3)

        self.formLayout_2.setWidget(32, QFormLayout.FieldRole, self.valueLabel_32)

        self.valueLabel_33 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_33.setObjectName(u"valueLabel_33")
        self.valueLabel_33.setFont(font3)

        self.formLayout_2.setWidget(33, QFormLayout.FieldRole, self.valueLabel_33)

        self.valueLabel_34 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_34.setObjectName(u"valueLabel_34")
        self.valueLabel_34.setFont(font3)

        self.formLayout_2.setWidget(34, QFormLayout.FieldRole, self.valueLabel_34)

        self.valueLabel_35 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_35.setObjectName(u"valueLabel_35")
        self.valueLabel_35.setFont(font3)

        self.formLayout_2.setWidget(35, QFormLayout.FieldRole, self.valueLabel_35)

        self.valueLabel_36 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_36.setObjectName(u"valueLabel_36")
        self.valueLabel_36.setFont(font3)

        self.formLayout_2.setWidget(36, QFormLayout.FieldRole, self.valueLabel_36)

        self.valueLabel_37 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_37.setObjectName(u"valueLabel_37")
        self.valueLabel_37.setFont(font3)

        self.formLayout_2.setWidget(37, QFormLayout.FieldRole, self.valueLabel_37)

        self.valueLabel_38 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_38.setObjectName(u"valueLabel_38")
        self.valueLabel_38.setFont(font3)

        self.formLayout_2.setWidget(38, QFormLayout.FieldRole, self.valueLabel_38)

        self.valueLabel_39 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_39.setObjectName(u"valueLabel_39")
        self.valueLabel_39.setFont(font3)

        self.formLayout_2.setWidget(39, QFormLayout.FieldRole, self.valueLabel_39)

        self.valueLabel_40 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_40.setObjectName(u"valueLabel_40")
        self.valueLabel_40.setFont(font3)

        self.formLayout_2.setWidget(40, QFormLayout.FieldRole, self.valueLabel_40)

        self.addrLabel_41 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_41.setObjectName(u"addrLabel_41")
        self.addrLabel_41.setFont(font3)

        self.formLayout_2.setWidget(41, QFormLayout.LabelRole, self.addrLabel_41)

        self.addrLabel_42 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_42.setObjectName(u"addrLabel_42")
        self.addrLabel_42.setFont(font3)

        self.formLayout_2.setWidget(42, QFormLayout.LabelRole, self.addrLabel_42)

        self.addrLabel_43 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_43.setObjectName(u"addrLabel_43")
        self.addrLabel_43.setFont(font3)

        self.formLayout_2.setWidget(43, QFormLayout.LabelRole, self.addrLabel_43)

        self.addrLabel_44 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_44.setObjectName(u"addrLabel_44")
        self.addrLabel_44.setFont(font3)

        self.formLayout_2.setWidget(44, QFormLayout.LabelRole, self.addrLabel_44)

        self.addrLabel_45 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_45.setObjectName(u"addrLabel_45")
        self.addrLabel_45.setFont(font3)

        self.formLayout_2.setWidget(45, QFormLayout.LabelRole, self.addrLabel_45)

        self.addrLabel_46 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_46.setObjectName(u"addrLabel_46")
        self.addrLabel_46.setFont(font3)

        self.formLayout_2.setWidget(46, QFormLayout.LabelRole, self.addrLabel_46)

        self.addrLabel_47 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_47.setObjectName(u"addrLabel_47")
        self.addrLabel_47.setFont(font3)

        self.formLayout_2.setWidget(47, QFormLayout.LabelRole, self.addrLabel_47)

        self.addrLabel_48 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_48.setObjectName(u"addrLabel_48")
        self.addrLabel_48.setFont(font3)

        self.formLayout_2.setWidget(48, QFormLayout.LabelRole, self.addrLabel_48)

        self.addrLabel_49 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_49.setObjectName(u"addrLabel_49")
        self.addrLabel_49.setFont(font3)

        self.formLayout_2.setWidget(49, QFormLayout.LabelRole, self.addrLabel_49)

        self.addrLabel_50 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_50.setObjectName(u"addrLabel_50")
        self.addrLabel_50.setFont(font3)

        self.formLayout_2.setWidget(50, QFormLayout.LabelRole, self.addrLabel_50)

        self.valueLabel_41 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_41.setObjectName(u"valueLabel_41")
        self.valueLabel_41.setFont(font3)

        self.formLayout_2.setWidget(41, QFormLayout.FieldRole, self.valueLabel_41)

        self.valueLabel_42 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_42.setObjectName(u"valueLabel_42")
        self.valueLabel_42.setFont(font3)

        self.formLayout_2.setWidget(42, QFormLayout.FieldRole, self.valueLabel_42)

        self.valueLabel_43 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_43.setObjectName(u"valueLabel_43")
        self.valueLabel_43.setFont(font3)

        self.formLayout_2.setWidget(43, QFormLayout.FieldRole, self.valueLabel_43)

        self.valueLabel_44 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_44.setObjectName(u"valueLabel_44")
        self.valueLabel_44.setFont(font3)

        self.formLayout_2.setWidget(44, QFormLayout.FieldRole, self.valueLabel_44)

        self.valueLabel_45 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_45.setObjectName(u"valueLabel_45")
        self.valueLabel_45.setFont(font3)

        self.formLayout_2.setWidget(45, QFormLayout.FieldRole, self.valueLabel_45)

        self.valueLabel_46 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_46.setObjectName(u"valueLabel_46")
        self.valueLabel_46.setFont(font3)

        self.formLayout_2.setWidget(46, QFormLayout.FieldRole, self.valueLabel_46)

        self.valueLabel_47 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_47.setObjectName(u"valueLabel_47")
        self.valueLabel_47.setFont(font3)

        self.formLayout_2.setWidget(47, QFormLayout.FieldRole, self.valueLabel_47)

        self.valueLabel_48 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_48.setObjectName(u"valueLabel_48")
        self.valueLabel_48.setFont(font3)

        self.formLayout_2.setWidget(48, QFormLayout.FieldRole, self.valueLabel_48)

        self.valueLabel_49 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_49.setObjectName(u"valueLabel_49")
        self.valueLabel_49.setFont(font3)

        self.formLayout_2.setWidget(49, QFormLayout.FieldRole, self.valueLabel_49)

        self.valueLabel_50 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_50.setObjectName(u"valueLabel_50")
        self.valueLabel_50.setFont(font3)

        self.formLayout_2.setWidget(50, QFormLayout.FieldRole, self.valueLabel_50)

        self.addrLabel_51 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_51.setObjectName(u"addrLabel_51")
        self.addrLabel_51.setFont(font3)

        self.formLayout_2.setWidget(51, QFormLayout.LabelRole, self.addrLabel_51)

        self.addrLabel_52 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_52.setObjectName(u"addrLabel_52")
        self.addrLabel_52.setFont(font3)

        self.formLayout_2.setWidget(52, QFormLayout.LabelRole, self.addrLabel_52)

        self.addrLabel_53 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_53.setObjectName(u"addrLabel_53")
        self.addrLabel_53.setFont(font3)

        self.formLayout_2.setWidget(53, QFormLayout.LabelRole, self.addrLabel_53)

        self.addrLabel_54 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_54.setObjectName(u"addrLabel_54")
        self.addrLabel_54.setFont(font3)

        self.formLayout_2.setWidget(54, QFormLayout.LabelRole, self.addrLabel_54)

        self.addrLabel_55 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_55.setObjectName(u"addrLabel_55")
        self.addrLabel_55.setFont(font3)

        self.formLayout_2.setWidget(55, QFormLayout.LabelRole, self.addrLabel_55)

        self.addrLabel_56 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_56.setObjectName(u"addrLabel_56")
        self.addrLabel_56.setFont(font3)

        self.formLayout_2.setWidget(56, QFormLayout.LabelRole, self.addrLabel_56)

        self.addrLabel_57 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_57.setObjectName(u"addrLabel_57")
        self.addrLabel_57.setFont(font3)

        self.formLayout_2.setWidget(57, QFormLayout.LabelRole, self.addrLabel_57)

        self.addrLabel_58 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_58.setObjectName(u"addrLabel_58")
        self.addrLabel_58.setFont(font3)

        self.formLayout_2.setWidget(58, QFormLayout.LabelRole, self.addrLabel_58)

        self.addrLabel_59 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_59.setObjectName(u"addrLabel_59")
        self.addrLabel_59.setFont(font3)

        self.formLayout_2.setWidget(59, QFormLayout.LabelRole, self.addrLabel_59)

        self.addrLabel_60 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_60.setObjectName(u"addrLabel_60")
        self.addrLabel_60.setFont(font3)

        self.formLayout_2.setWidget(60, QFormLayout.LabelRole, self.addrLabel_60)

        self.valueLabel_51 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_51.setObjectName(u"valueLabel_51")
        self.valueLabel_51.setFont(font3)

        self.formLayout_2.setWidget(51, QFormLayout.FieldRole, self.valueLabel_51)

        self.valueLabel_52 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_52.setObjectName(u"valueLabel_52")
        self.valueLabel_52.setFont(font3)

        self.formLayout_2.setWidget(52, QFormLayout.FieldRole, self.valueLabel_52)

        self.valueLabel_53 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_53.setObjectName(u"valueLabel_53")
        self.valueLabel_53.setFont(font3)

        self.formLayout_2.setWidget(53, QFormLayout.FieldRole, self.valueLabel_53)

        self.valueLabel_54 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_54.setObjectName(u"valueLabel_54")
        self.valueLabel_54.setFont(font3)

        self.formLayout_2.setWidget(54, QFormLayout.FieldRole, self.valueLabel_54)

        self.valueLabel_55 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_55.setObjectName(u"valueLabel_55")
        self.valueLabel_55.setFont(font3)

        self.formLayout_2.setWidget(55, QFormLayout.FieldRole, self.valueLabel_55)

        self.valueLabel_56 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_56.setObjectName(u"valueLabel_56")
        self.valueLabel_56.setFont(font3)

        self.formLayout_2.setWidget(56, QFormLayout.FieldRole, self.valueLabel_56)

        self.valueLabel_57 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_57.setObjectName(u"valueLabel_57")
        self.valueLabel_57.setFont(font3)

        self.formLayout_2.setWidget(57, QFormLayout.FieldRole, self.valueLabel_57)

        self.valueLabel_58 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_58.setObjectName(u"valueLabel_58")
        self.valueLabel_58.setFont(font3)

        self.formLayout_2.setWidget(58, QFormLayout.FieldRole, self.valueLabel_58)

        self.valueLabel_59 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_59.setObjectName(u"valueLabel_59")
        self.valueLabel_59.setFont(font3)

        self.formLayout_2.setWidget(59, QFormLayout.FieldRole, self.valueLabel_59)

        self.valueLabel_60 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_60.setObjectName(u"valueLabel_60")
        self.valueLabel_60.setFont(font3)

        self.formLayout_2.setWidget(60, QFormLayout.FieldRole, self.valueLabel_60)

        self.addrLabel_61 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_61.setObjectName(u"addrLabel_61")
        self.addrLabel_61.setFont(font3)

        self.formLayout_2.setWidget(61, QFormLayout.LabelRole, self.addrLabel_61)

        self.addrLabel_62 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_62.setObjectName(u"addrLabel_62")
        self.addrLabel_62.setFont(font3)

        self.formLayout_2.setWidget(62, QFormLayout.LabelRole, self.addrLabel_62)

        self.addrLabel_63 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_63.setObjectName(u"addrLabel_63")
        self.addrLabel_63.setFont(font3)

        self.formLayout_2.setWidget(63, QFormLayout.LabelRole, self.addrLabel_63)

        self.addrLabel_64 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_64.setObjectName(u"addrLabel_64")
        self.addrLabel_64.setFont(font3)

        self.formLayout_2.setWidget(64, QFormLayout.LabelRole, self.addrLabel_64)

        self.addrLabel_65 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_65.setObjectName(u"addrLabel_65")
        self.addrLabel_65.setFont(font3)

        self.formLayout_2.setWidget(65, QFormLayout.LabelRole, self.addrLabel_65)

        self.addrLabel_66 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_66.setObjectName(u"addrLabel_66")
        self.addrLabel_66.setFont(font3)

        self.formLayout_2.setWidget(66, QFormLayout.LabelRole, self.addrLabel_66)

        self.addrLabel_67 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_67.setObjectName(u"addrLabel_67")
        self.addrLabel_67.setFont(font3)

        self.formLayout_2.setWidget(67, QFormLayout.LabelRole, self.addrLabel_67)

        self.addrLabel_68 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_68.setObjectName(u"addrLabel_68")
        self.addrLabel_68.setFont(font3)

        self.formLayout_2.setWidget(68, QFormLayout.LabelRole, self.addrLabel_68)

        self.addrLabel_69 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_69.setObjectName(u"addrLabel_69")
        self.addrLabel_69.setFont(font3)

        self.formLayout_2.setWidget(69, QFormLayout.LabelRole, self.addrLabel_69)

        self.addrLabel_70 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_70.setObjectName(u"addrLabel_70")
        self.addrLabel_70.setFont(font3)

        self.formLayout_2.setWidget(70, QFormLayout.LabelRole, self.addrLabel_70)

        self.valueLabel_61 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_61.setObjectName(u"valueLabel_61")
        self.valueLabel_61.setFont(font3)

        self.formLayout_2.setWidget(61, QFormLayout.FieldRole, self.valueLabel_61)

        self.valueLabel_62 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_62.setObjectName(u"valueLabel_62")
        self.valueLabel_62.setFont(font3)

        self.formLayout_2.setWidget(62, QFormLayout.FieldRole, self.valueLabel_62)

        self.valueLabel_63 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_63.setObjectName(u"valueLabel_63")
        self.valueLabel_63.setFont(font3)

        self.formLayout_2.setWidget(63, QFormLayout.FieldRole, self.valueLabel_63)

        self.valueLabel_64 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_64.setObjectName(u"valueLabel_64")
        self.valueLabel_64.setFont(font3)

        self.formLayout_2.setWidget(64, QFormLayout.FieldRole, self.valueLabel_64)

        self.valueLabel_65 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_65.setObjectName(u"valueLabel_65")
        self.valueLabel_65.setFont(font3)

        self.formLayout_2.setWidget(65, QFormLayout.FieldRole, self.valueLabel_65)

        self.valueLabel_66 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_66.setObjectName(u"valueLabel_66")
        self.valueLabel_66.setFont(font3)

        self.formLayout_2.setWidget(66, QFormLayout.FieldRole, self.valueLabel_66)

        self.valueLabel_67 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_67.setObjectName(u"valueLabel_67")
        self.valueLabel_67.setFont(font3)

        self.formLayout_2.setWidget(67, QFormLayout.FieldRole, self.valueLabel_67)

        self.valueLabel_68 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_68.setObjectName(u"valueLabel_68")
        self.valueLabel_68.setFont(font3)

        self.formLayout_2.setWidget(68, QFormLayout.FieldRole, self.valueLabel_68)

        self.valueLabel_69 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_69.setObjectName(u"valueLabel_69")
        self.valueLabel_69.setFont(font3)

        self.formLayout_2.setWidget(69, QFormLayout.FieldRole, self.valueLabel_69)

        self.valueLabel_70 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_70.setObjectName(u"valueLabel_70")
        self.valueLabel_70.setFont(font3)

        self.formLayout_2.setWidget(70, QFormLayout.FieldRole, self.valueLabel_70)

        self.addrLabel_71 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_71.setObjectName(u"addrLabel_71")
        self.addrLabel_71.setFont(font3)

        self.formLayout_2.setWidget(71, QFormLayout.LabelRole, self.addrLabel_71)

        self.addrLabel_72 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_72.setObjectName(u"addrLabel_72")
        self.addrLabel_72.setFont(font3)

        self.formLayout_2.setWidget(72, QFormLayout.LabelRole, self.addrLabel_72)

        self.addrLabel_73 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_73.setObjectName(u"addrLabel_73")
        self.addrLabel_73.setFont(font3)

        self.formLayout_2.setWidget(73, QFormLayout.LabelRole, self.addrLabel_73)

        self.addrLabel_74 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_74.setObjectName(u"addrLabel_74")
        self.addrLabel_74.setFont(font3)

        self.formLayout_2.setWidget(74, QFormLayout.LabelRole, self.addrLabel_74)

        self.addrLabel_75 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_75.setObjectName(u"addrLabel_75")
        self.addrLabel_75.setFont(font3)

        self.formLayout_2.setWidget(75, QFormLayout.LabelRole, self.addrLabel_75)

        self.addrLabel_76 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_76.setObjectName(u"addrLabel_76")
        self.addrLabel_76.setFont(font3)

        self.formLayout_2.setWidget(76, QFormLayout.LabelRole, self.addrLabel_76)

        self.addrLabel_77 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_77.setObjectName(u"addrLabel_77")
        self.addrLabel_77.setFont(font3)

        self.formLayout_2.setWidget(77, QFormLayout.LabelRole, self.addrLabel_77)

        self.addrLabel_78 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_78.setObjectName(u"addrLabel_78")
        self.addrLabel_78.setFont(font3)

        self.formLayout_2.setWidget(78, QFormLayout.LabelRole, self.addrLabel_78)

        self.addrLabel_79 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_79.setObjectName(u"addrLabel_79")
        self.addrLabel_79.setFont(font3)

        self.formLayout_2.setWidget(79, QFormLayout.LabelRole, self.addrLabel_79)

        self.addrLabel_80 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_80.setObjectName(u"addrLabel_80")
        self.addrLabel_80.setFont(font3)

        self.formLayout_2.setWidget(80, QFormLayout.LabelRole, self.addrLabel_80)

        self.valueLabel_71 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_71.setObjectName(u"valueLabel_71")
        self.valueLabel_71.setFont(font3)

        self.formLayout_2.setWidget(71, QFormLayout.FieldRole, self.valueLabel_71)

        self.valueLabel_72 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_72.setObjectName(u"valueLabel_72")
        self.valueLabel_72.setFont(font3)

        self.formLayout_2.setWidget(72, QFormLayout.FieldRole, self.valueLabel_72)

        self.valueLabel_73 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_73.setObjectName(u"valueLabel_73")
        self.valueLabel_73.setFont(font3)

        self.formLayout_2.setWidget(73, QFormLayout.FieldRole, self.valueLabel_73)

        self.valueLabel_74 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_74.setObjectName(u"valueLabel_74")
        self.valueLabel_74.setFont(font3)

        self.formLayout_2.setWidget(74, QFormLayout.FieldRole, self.valueLabel_74)

        self.valueLabel_75 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_75.setObjectName(u"valueLabel_75")
        self.valueLabel_75.setFont(font3)

        self.formLayout_2.setWidget(75, QFormLayout.FieldRole, self.valueLabel_75)

        self.valueLabel_76 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_76.setObjectName(u"valueLabel_76")
        self.valueLabel_76.setFont(font3)

        self.formLayout_2.setWidget(76, QFormLayout.FieldRole, self.valueLabel_76)

        self.valueLabel_77 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_77.setObjectName(u"valueLabel_77")
        self.valueLabel_77.setFont(font3)

        self.formLayout_2.setWidget(77, QFormLayout.FieldRole, self.valueLabel_77)

        self.valueLabel_78 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_78.setObjectName(u"valueLabel_78")
        self.valueLabel_78.setFont(font3)

        self.formLayout_2.setWidget(78, QFormLayout.FieldRole, self.valueLabel_78)

        self.valueLabel_79 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_79.setObjectName(u"valueLabel_79")
        self.valueLabel_79.setFont(font3)

        self.formLayout_2.setWidget(79, QFormLayout.FieldRole, self.valueLabel_79)

        self.valueLabel_80 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_80.setObjectName(u"valueLabel_80")
        self.valueLabel_80.setFont(font3)

        self.formLayout_2.setWidget(80, QFormLayout.FieldRole, self.valueLabel_80)

        self.memoriaArea.setWidget(self.scrollAreaWidgetContents_2)
        self.memoriaMainLabel = QLabel(self.centralwidget)
        self.memoriaMainLabel.setObjectName(u"memoriaMainLabel")
        self.memoriaMainLabel.setGeometry(QRect(820, 540, 71, 31))
        self.memoriaMainLabel.setFont(font4)
        self.memoriaArea_2 = QScrollArea(self.centralwidget)
        self.memoriaArea_2.setObjectName(u"memoriaArea_2")
        self.memoriaArea_2.setGeometry(QRect(620, 90, 161, 331))
        self.memoriaArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 142, 1798))
        self.formLayout_3 = QFormLayout(self.scrollAreaWidgetContents_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.rxMainLabel_4 = QLabel(self.scrollAreaWidgetContents_3)
        self.rxMainLabel_4.setObjectName(u"rxMainLabel_4")
        self.rxMainLabel_4.setFont(font2)
        self.rxMainLabel_4.setTextFormat(Qt.AutoText)
        self.rxMainLabel_4.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.rxMainLabel_4)

        self.valueRegistrosLabel_4 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueRegistrosLabel_4.setObjectName(u"valueRegistrosLabel_4")
        self.valueRegistrosLabel_4.setFont(font2)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.valueRegistrosLabel_4)

        self.addrLabel_81 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_81.setObjectName(u"addrLabel_81")
        self.addrLabel_81.setFont(font3)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.addrLabel_81)

        self.valueLabel_81 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_81.setObjectName(u"valueLabel_81")
        self.valueLabel_81.setFont(font3)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.valueLabel_81)

        self.addrLabel_82 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_82.setObjectName(u"addrLabel_82")
        self.addrLabel_82.setFont(font3)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.addrLabel_82)

        self.valueLabel_82 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_82.setObjectName(u"valueLabel_82")
        self.valueLabel_82.setFont(font3)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.valueLabel_82)

        self.addrLabel_83 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_83.setObjectName(u"addrLabel_83")
        self.addrLabel_83.setFont(font3)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.addrLabel_83)

        self.valueLabel_83 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_83.setObjectName(u"valueLabel_83")
        self.valueLabel_83.setFont(font3)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.valueLabel_83)

        self.addrLabel_84 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_84.setObjectName(u"addrLabel_84")
        self.addrLabel_84.setFont(font3)

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.addrLabel_84)

        self.valueLabel_84 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_84.setObjectName(u"valueLabel_84")
        self.valueLabel_84.setFont(font3)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.valueLabel_84)

        self.addrLabel_85 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_85.setObjectName(u"addrLabel_85")
        self.addrLabel_85.setFont(font3)

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.addrLabel_85)

        self.valueLabel_85 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_85.setObjectName(u"valueLabel_85")
        self.valueLabel_85.setFont(font3)

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.valueLabel_85)

        self.addrLabel_86 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_86.setObjectName(u"addrLabel_86")
        self.addrLabel_86.setFont(font3)

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.addrLabel_86)

        self.valueLabel_86 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_86.setObjectName(u"valueLabel_86")
        self.valueLabel_86.setFont(font3)

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.valueLabel_86)

        self.addrLabel_87 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_87.setObjectName(u"addrLabel_87")
        self.addrLabel_87.setFont(font3)

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.addrLabel_87)

        self.valueLabel_87 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_87.setObjectName(u"valueLabel_87")
        self.valueLabel_87.setFont(font3)

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.valueLabel_87)

        self.addrLabel_88 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_88.setObjectName(u"addrLabel_88")
        self.addrLabel_88.setFont(font3)

        self.formLayout_3.setWidget(8, QFormLayout.LabelRole, self.addrLabel_88)

        self.valueLabel_88 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_88.setObjectName(u"valueLabel_88")
        self.valueLabel_88.setFont(font3)

        self.formLayout_3.setWidget(8, QFormLayout.FieldRole, self.valueLabel_88)

        self.addrLabel_89 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_89.setObjectName(u"addrLabel_89")
        self.addrLabel_89.setFont(font3)

        self.formLayout_3.setWidget(9, QFormLayout.LabelRole, self.addrLabel_89)

        self.valueLabel_89 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_89.setObjectName(u"valueLabel_89")
        self.valueLabel_89.setFont(font3)

        self.formLayout_3.setWidget(9, QFormLayout.FieldRole, self.valueLabel_89)

        self.addrLabel_90 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_90.setObjectName(u"addrLabel_90")
        self.addrLabel_90.setFont(font3)

        self.formLayout_3.setWidget(10, QFormLayout.LabelRole, self.addrLabel_90)

        self.valueLabel_90 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_90.setObjectName(u"valueLabel_90")
        self.valueLabel_90.setFont(font3)

        self.formLayout_3.setWidget(10, QFormLayout.FieldRole, self.valueLabel_90)

        self.addrLabel_91 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_91.setObjectName(u"addrLabel_91")
        self.addrLabel_91.setFont(font3)

        self.formLayout_3.setWidget(11, QFormLayout.LabelRole, self.addrLabel_91)

        self.valueLabel_91 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_91.setObjectName(u"valueLabel_91")
        self.valueLabel_91.setFont(font3)

        self.formLayout_3.setWidget(11, QFormLayout.FieldRole, self.valueLabel_91)

        self.addrLabel_92 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_92.setObjectName(u"addrLabel_92")
        self.addrLabel_92.setFont(font3)

        self.formLayout_3.setWidget(12, QFormLayout.LabelRole, self.addrLabel_92)

        self.valueLabel_92 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_92.setObjectName(u"valueLabel_92")
        self.valueLabel_92.setFont(font3)

        self.formLayout_3.setWidget(12, QFormLayout.FieldRole, self.valueLabel_92)

        self.addrLabel_93 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_93.setObjectName(u"addrLabel_93")
        self.addrLabel_93.setFont(font3)

        self.formLayout_3.setWidget(13, QFormLayout.LabelRole, self.addrLabel_93)

        self.valueLabel_93 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_93.setObjectName(u"valueLabel_93")
        self.valueLabel_93.setFont(font3)

        self.formLayout_3.setWidget(13, QFormLayout.FieldRole, self.valueLabel_93)

        self.addrLabel_94 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_94.setObjectName(u"addrLabel_94")
        self.addrLabel_94.setFont(font3)

        self.formLayout_3.setWidget(14, QFormLayout.LabelRole, self.addrLabel_94)

        self.valueLabel_94 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_94.setObjectName(u"valueLabel_94")
        self.valueLabel_94.setFont(font3)

        self.formLayout_3.setWidget(14, QFormLayout.FieldRole, self.valueLabel_94)

        self.addrLabel_95 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_95.setObjectName(u"addrLabel_95")
        self.addrLabel_95.setFont(font3)

        self.formLayout_3.setWidget(15, QFormLayout.LabelRole, self.addrLabel_95)

        self.valueLabel_95 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_95.setObjectName(u"valueLabel_95")
        self.valueLabel_95.setFont(font3)

        self.formLayout_3.setWidget(15, QFormLayout.FieldRole, self.valueLabel_95)

        self.addrLabel_96 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_96.setObjectName(u"addrLabel_96")
        self.addrLabel_96.setFont(font3)

        self.formLayout_3.setWidget(16, QFormLayout.LabelRole, self.addrLabel_96)

        self.valueLabel_96 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_96.setObjectName(u"valueLabel_96")
        self.valueLabel_96.setFont(font3)

        self.formLayout_3.setWidget(16, QFormLayout.FieldRole, self.valueLabel_96)

        self.addrLabel_97 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_97.setObjectName(u"addrLabel_97")
        self.addrLabel_97.setFont(font3)

        self.formLayout_3.setWidget(17, QFormLayout.LabelRole, self.addrLabel_97)

        self.valueLabel_97 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_97.setObjectName(u"valueLabel_97")
        self.valueLabel_97.setFont(font3)

        self.formLayout_3.setWidget(17, QFormLayout.FieldRole, self.valueLabel_97)

        self.addrLabel_98 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_98.setObjectName(u"addrLabel_98")
        self.addrLabel_98.setFont(font3)

        self.formLayout_3.setWidget(18, QFormLayout.LabelRole, self.addrLabel_98)

        self.valueLabel_98 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_98.setObjectName(u"valueLabel_98")
        self.valueLabel_98.setFont(font3)

        self.formLayout_3.setWidget(18, QFormLayout.FieldRole, self.valueLabel_98)

        self.addrLabel_99 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_99.setObjectName(u"addrLabel_99")
        self.addrLabel_99.setFont(font3)

        self.formLayout_3.setWidget(19, QFormLayout.LabelRole, self.addrLabel_99)

        self.valueLabel_99 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_99.setObjectName(u"valueLabel_99")
        self.valueLabel_99.setFont(font3)

        self.formLayout_3.setWidget(19, QFormLayout.FieldRole, self.valueLabel_99)

        self.addrLabel_100 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_100.setObjectName(u"addrLabel_100")
        self.addrLabel_100.setFont(font3)

        self.formLayout_3.setWidget(20, QFormLayout.LabelRole, self.addrLabel_100)

        self.valueLabel_100 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_100.setObjectName(u"valueLabel_100")
        self.valueLabel_100.setFont(font3)

        self.formLayout_3.setWidget(20, QFormLayout.FieldRole, self.valueLabel_100)

        self.addrLabel_101 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_101.setObjectName(u"addrLabel_101")
        self.addrLabel_101.setFont(font3)

        self.formLayout_3.setWidget(21, QFormLayout.LabelRole, self.addrLabel_101)

        self.valueLabel_101 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_101.setObjectName(u"valueLabel_101")
        self.valueLabel_101.setFont(font3)

        self.formLayout_3.setWidget(21, QFormLayout.FieldRole, self.valueLabel_101)

        self.valueLabel_102 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_102.setObjectName(u"valueLabel_102")
        self.valueLabel_102.setFont(font3)

        self.formLayout_3.setWidget(22, QFormLayout.FieldRole, self.valueLabel_102)

        self.valueLabel_103 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_103.setObjectName(u"valueLabel_103")
        self.valueLabel_103.setFont(font3)

        self.formLayout_3.setWidget(23, QFormLayout.FieldRole, self.valueLabel_103)

        self.valueLabel_104 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_104.setObjectName(u"valueLabel_104")
        self.valueLabel_104.setFont(font3)

        self.formLayout_3.setWidget(31, QFormLayout.FieldRole, self.valueLabel_104)

        self.valueLabel_105 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_105.setObjectName(u"valueLabel_105")
        self.valueLabel_105.setFont(font3)

        self.formLayout_3.setWidget(30, QFormLayout.FieldRole, self.valueLabel_105)

        self.valueLabel_106 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_106.setObjectName(u"valueLabel_106")
        self.valueLabel_106.setFont(font3)

        self.formLayout_3.setWidget(29, QFormLayout.FieldRole, self.valueLabel_106)

        self.valueLabel_107 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_107.setObjectName(u"valueLabel_107")
        self.valueLabel_107.setFont(font3)

        self.formLayout_3.setWidget(28, QFormLayout.FieldRole, self.valueLabel_107)

        self.valueLabel_108 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_108.setObjectName(u"valueLabel_108")
        self.valueLabel_108.setFont(font3)

        self.formLayout_3.setWidget(27, QFormLayout.FieldRole, self.valueLabel_108)

        self.valueLabel_109 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_109.setObjectName(u"valueLabel_109")
        self.valueLabel_109.setFont(font3)

        self.formLayout_3.setWidget(26, QFormLayout.FieldRole, self.valueLabel_109)

        self.valueLabel_110 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_110.setObjectName(u"valueLabel_110")
        self.valueLabel_110.setFont(font3)

        self.formLayout_3.setWidget(25, QFormLayout.FieldRole, self.valueLabel_110)

        self.valueLabel_111 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_111.setObjectName(u"valueLabel_111")
        self.valueLabel_111.setFont(font3)

        self.formLayout_3.setWidget(24, QFormLayout.FieldRole, self.valueLabel_111)

        self.addrLabel_102 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_102.setObjectName(u"addrLabel_102")
        self.addrLabel_102.setFont(font3)

        self.formLayout_3.setWidget(22, QFormLayout.LabelRole, self.addrLabel_102)

        self.addrLabel_103 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_103.setObjectName(u"addrLabel_103")
        self.addrLabel_103.setFont(font3)

        self.formLayout_3.setWidget(23, QFormLayout.LabelRole, self.addrLabel_103)

        self.addrLabel_104 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_104.setObjectName(u"addrLabel_104")
        self.addrLabel_104.setFont(font3)

        self.formLayout_3.setWidget(24, QFormLayout.LabelRole, self.addrLabel_104)

        self.addrLabel_105 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_105.setObjectName(u"addrLabel_105")
        self.addrLabel_105.setFont(font3)

        self.formLayout_3.setWidget(25, QFormLayout.LabelRole, self.addrLabel_105)

        self.addrLabel_106 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_106.setObjectName(u"addrLabel_106")
        self.addrLabel_106.setFont(font3)

        self.formLayout_3.setWidget(26, QFormLayout.LabelRole, self.addrLabel_106)

        self.addrLabel_107 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_107.setObjectName(u"addrLabel_107")
        self.addrLabel_107.setFont(font3)

        self.formLayout_3.setWidget(27, QFormLayout.LabelRole, self.addrLabel_107)

        self.addrLabel_108 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_108.setObjectName(u"addrLabel_108")
        self.addrLabel_108.setFont(font3)

        self.formLayout_3.setWidget(28, QFormLayout.LabelRole, self.addrLabel_108)

        self.addrLabel_109 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_109.setObjectName(u"addrLabel_109")
        self.addrLabel_109.setFont(font3)

        self.formLayout_3.setWidget(29, QFormLayout.LabelRole, self.addrLabel_109)

        self.addrLabel_110 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_110.setObjectName(u"addrLabel_110")
        self.addrLabel_110.setFont(font3)

        self.formLayout_3.setWidget(30, QFormLayout.LabelRole, self.addrLabel_110)

        self.addrLabel_111 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_111.setObjectName(u"addrLabel_111")
        self.addrLabel_111.setFont(font3)

        self.formLayout_3.setWidget(31, QFormLayout.LabelRole, self.addrLabel_111)

        self.addrLabel_112 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_112.setObjectName(u"addrLabel_112")
        self.addrLabel_112.setFont(font3)

        self.formLayout_3.setWidget(32, QFormLayout.LabelRole, self.addrLabel_112)

        self.addrLabel_113 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_113.setObjectName(u"addrLabel_113")
        self.addrLabel_113.setFont(font3)

        self.formLayout_3.setWidget(33, QFormLayout.LabelRole, self.addrLabel_113)

        self.addrLabel_114 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_114.setObjectName(u"addrLabel_114")
        self.addrLabel_114.setFont(font3)

        self.formLayout_3.setWidget(34, QFormLayout.LabelRole, self.addrLabel_114)

        self.addrLabel_115 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_115.setObjectName(u"addrLabel_115")
        self.addrLabel_115.setFont(font3)

        self.formLayout_3.setWidget(35, QFormLayout.LabelRole, self.addrLabel_115)

        self.addrLabel_116 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_116.setObjectName(u"addrLabel_116")
        self.addrLabel_116.setFont(font3)

        self.formLayout_3.setWidget(36, QFormLayout.LabelRole, self.addrLabel_116)

        self.addrLabel_117 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_117.setObjectName(u"addrLabel_117")
        self.addrLabel_117.setFont(font3)

        self.formLayout_3.setWidget(37, QFormLayout.LabelRole, self.addrLabel_117)

        self.addrLabel_118 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_118.setObjectName(u"addrLabel_118")
        self.addrLabel_118.setFont(font3)

        self.formLayout_3.setWidget(38, QFormLayout.LabelRole, self.addrLabel_118)

        self.addrLabel_119 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_119.setObjectName(u"addrLabel_119")
        self.addrLabel_119.setFont(font3)

        self.formLayout_3.setWidget(39, QFormLayout.LabelRole, self.addrLabel_119)

        self.addrLabel_120 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_120.setObjectName(u"addrLabel_120")
        self.addrLabel_120.setFont(font3)

        self.formLayout_3.setWidget(40, QFormLayout.LabelRole, self.addrLabel_120)

        self.valueLabel_112 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_112.setObjectName(u"valueLabel_112")
        self.valueLabel_112.setFont(font3)

        self.formLayout_3.setWidget(32, QFormLayout.FieldRole, self.valueLabel_112)

        self.valueLabel_113 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_113.setObjectName(u"valueLabel_113")
        self.valueLabel_113.setFont(font3)

        self.formLayout_3.setWidget(33, QFormLayout.FieldRole, self.valueLabel_113)

        self.valueLabel_114 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_114.setObjectName(u"valueLabel_114")
        self.valueLabel_114.setFont(font3)

        self.formLayout_3.setWidget(34, QFormLayout.FieldRole, self.valueLabel_114)

        self.valueLabel_115 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_115.setObjectName(u"valueLabel_115")
        self.valueLabel_115.setFont(font3)

        self.formLayout_3.setWidget(35, QFormLayout.FieldRole, self.valueLabel_115)

        self.valueLabel_116 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_116.setObjectName(u"valueLabel_116")
        self.valueLabel_116.setFont(font3)

        self.formLayout_3.setWidget(36, QFormLayout.FieldRole, self.valueLabel_116)

        self.valueLabel_117 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_117.setObjectName(u"valueLabel_117")
        self.valueLabel_117.setFont(font3)

        self.formLayout_3.setWidget(37, QFormLayout.FieldRole, self.valueLabel_117)

        self.valueLabel_118 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_118.setObjectName(u"valueLabel_118")
        self.valueLabel_118.setFont(font3)

        self.formLayout_3.setWidget(38, QFormLayout.FieldRole, self.valueLabel_118)

        self.valueLabel_119 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_119.setObjectName(u"valueLabel_119")
        self.valueLabel_119.setFont(font3)

        self.formLayout_3.setWidget(39, QFormLayout.FieldRole, self.valueLabel_119)

        self.valueLabel_120 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_120.setObjectName(u"valueLabel_120")
        self.valueLabel_120.setFont(font3)

        self.formLayout_3.setWidget(40, QFormLayout.FieldRole, self.valueLabel_120)

        self.addrLabel_121 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_121.setObjectName(u"addrLabel_121")
        self.addrLabel_121.setFont(font3)

        self.formLayout_3.setWidget(41, QFormLayout.LabelRole, self.addrLabel_121)

        self.addrLabel_122 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_122.setObjectName(u"addrLabel_122")
        self.addrLabel_122.setFont(font3)

        self.formLayout_3.setWidget(42, QFormLayout.LabelRole, self.addrLabel_122)

        self.addrLabel_123 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_123.setObjectName(u"addrLabel_123")
        self.addrLabel_123.setFont(font3)

        self.formLayout_3.setWidget(43, QFormLayout.LabelRole, self.addrLabel_123)

        self.addrLabel_124 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_124.setObjectName(u"addrLabel_124")
        self.addrLabel_124.setFont(font3)

        self.formLayout_3.setWidget(44, QFormLayout.LabelRole, self.addrLabel_124)

        self.addrLabel_125 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_125.setObjectName(u"addrLabel_125")
        self.addrLabel_125.setFont(font3)

        self.formLayout_3.setWidget(45, QFormLayout.LabelRole, self.addrLabel_125)

        self.addrLabel_126 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_126.setObjectName(u"addrLabel_126")
        self.addrLabel_126.setFont(font3)

        self.formLayout_3.setWidget(46, QFormLayout.LabelRole, self.addrLabel_126)

        self.addrLabel_127 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_127.setObjectName(u"addrLabel_127")
        self.addrLabel_127.setFont(font3)

        self.formLayout_3.setWidget(47, QFormLayout.LabelRole, self.addrLabel_127)

        self.addrLabel_128 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_128.setObjectName(u"addrLabel_128")
        self.addrLabel_128.setFont(font3)

        self.formLayout_3.setWidget(48, QFormLayout.LabelRole, self.addrLabel_128)

        self.addrLabel_129 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_129.setObjectName(u"addrLabel_129")
        self.addrLabel_129.setFont(font3)

        self.formLayout_3.setWidget(49, QFormLayout.LabelRole, self.addrLabel_129)

        self.addrLabel_130 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_130.setObjectName(u"addrLabel_130")
        self.addrLabel_130.setFont(font3)

        self.formLayout_3.setWidget(50, QFormLayout.LabelRole, self.addrLabel_130)

        self.valueLabel_121 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_121.setObjectName(u"valueLabel_121")
        self.valueLabel_121.setFont(font3)

        self.formLayout_3.setWidget(41, QFormLayout.FieldRole, self.valueLabel_121)

        self.valueLabel_122 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_122.setObjectName(u"valueLabel_122")
        self.valueLabel_122.setFont(font3)

        self.formLayout_3.setWidget(42, QFormLayout.FieldRole, self.valueLabel_122)

        self.valueLabel_123 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_123.setObjectName(u"valueLabel_123")
        self.valueLabel_123.setFont(font3)

        self.formLayout_3.setWidget(43, QFormLayout.FieldRole, self.valueLabel_123)

        self.valueLabel_124 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_124.setObjectName(u"valueLabel_124")
        self.valueLabel_124.setFont(font3)

        self.formLayout_3.setWidget(44, QFormLayout.FieldRole, self.valueLabel_124)

        self.valueLabel_125 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_125.setObjectName(u"valueLabel_125")
        self.valueLabel_125.setFont(font3)

        self.formLayout_3.setWidget(45, QFormLayout.FieldRole, self.valueLabel_125)

        self.valueLabel_126 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_126.setObjectName(u"valueLabel_126")
        self.valueLabel_126.setFont(font3)

        self.formLayout_3.setWidget(46, QFormLayout.FieldRole, self.valueLabel_126)

        self.valueLabel_127 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_127.setObjectName(u"valueLabel_127")
        self.valueLabel_127.setFont(font3)

        self.formLayout_3.setWidget(47, QFormLayout.FieldRole, self.valueLabel_127)

        self.valueLabel_128 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_128.setObjectName(u"valueLabel_128")
        self.valueLabel_128.setFont(font3)

        self.formLayout_3.setWidget(48, QFormLayout.FieldRole, self.valueLabel_128)

        self.valueLabel_129 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_129.setObjectName(u"valueLabel_129")
        self.valueLabel_129.setFont(font3)

        self.formLayout_3.setWidget(49, QFormLayout.FieldRole, self.valueLabel_129)

        self.valueLabel_130 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_130.setObjectName(u"valueLabel_130")
        self.valueLabel_130.setFont(font3)

        self.formLayout_3.setWidget(50, QFormLayout.FieldRole, self.valueLabel_130)

        self.addrLabel_131 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_131.setObjectName(u"addrLabel_131")
        self.addrLabel_131.setFont(font3)

        self.formLayout_3.setWidget(51, QFormLayout.LabelRole, self.addrLabel_131)

        self.addrLabel_132 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_132.setObjectName(u"addrLabel_132")
        self.addrLabel_132.setFont(font3)

        self.formLayout_3.setWidget(52, QFormLayout.LabelRole, self.addrLabel_132)

        self.addrLabel_133 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_133.setObjectName(u"addrLabel_133")
        self.addrLabel_133.setFont(font3)

        self.formLayout_3.setWidget(53, QFormLayout.LabelRole, self.addrLabel_133)

        self.addrLabel_134 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_134.setObjectName(u"addrLabel_134")
        self.addrLabel_134.setFont(font3)

        self.formLayout_3.setWidget(54, QFormLayout.LabelRole, self.addrLabel_134)

        self.addrLabel_135 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_135.setObjectName(u"addrLabel_135")
        self.addrLabel_135.setFont(font3)

        self.formLayout_3.setWidget(55, QFormLayout.LabelRole, self.addrLabel_135)

        self.addrLabel_136 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_136.setObjectName(u"addrLabel_136")
        self.addrLabel_136.setFont(font3)

        self.formLayout_3.setWidget(56, QFormLayout.LabelRole, self.addrLabel_136)

        self.addrLabel_137 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_137.setObjectName(u"addrLabel_137")
        self.addrLabel_137.setFont(font3)

        self.formLayout_3.setWidget(57, QFormLayout.LabelRole, self.addrLabel_137)

        self.addrLabel_138 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_138.setObjectName(u"addrLabel_138")
        self.addrLabel_138.setFont(font3)

        self.formLayout_3.setWidget(58, QFormLayout.LabelRole, self.addrLabel_138)

        self.addrLabel_139 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_139.setObjectName(u"addrLabel_139")
        self.addrLabel_139.setFont(font3)

        self.formLayout_3.setWidget(59, QFormLayout.LabelRole, self.addrLabel_139)

        self.addrLabel_140 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_140.setObjectName(u"addrLabel_140")
        self.addrLabel_140.setFont(font3)

        self.formLayout_3.setWidget(60, QFormLayout.LabelRole, self.addrLabel_140)

        self.valueLabel_131 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_131.setObjectName(u"valueLabel_131")
        self.valueLabel_131.setFont(font3)

        self.formLayout_3.setWidget(51, QFormLayout.FieldRole, self.valueLabel_131)

        self.valueLabel_132 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_132.setObjectName(u"valueLabel_132")
        self.valueLabel_132.setFont(font3)

        self.formLayout_3.setWidget(52, QFormLayout.FieldRole, self.valueLabel_132)

        self.valueLabel_133 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_133.setObjectName(u"valueLabel_133")
        self.valueLabel_133.setFont(font3)

        self.formLayout_3.setWidget(53, QFormLayout.FieldRole, self.valueLabel_133)

        self.valueLabel_134 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_134.setObjectName(u"valueLabel_134")
        self.valueLabel_134.setFont(font3)

        self.formLayout_3.setWidget(54, QFormLayout.FieldRole, self.valueLabel_134)

        self.valueLabel_135 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_135.setObjectName(u"valueLabel_135")
        self.valueLabel_135.setFont(font3)

        self.formLayout_3.setWidget(55, QFormLayout.FieldRole, self.valueLabel_135)

        self.valueLabel_136 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_136.setObjectName(u"valueLabel_136")
        self.valueLabel_136.setFont(font3)

        self.formLayout_3.setWidget(56, QFormLayout.FieldRole, self.valueLabel_136)

        self.valueLabel_137 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_137.setObjectName(u"valueLabel_137")
        self.valueLabel_137.setFont(font3)

        self.formLayout_3.setWidget(57, QFormLayout.FieldRole, self.valueLabel_137)

        self.valueLabel_138 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_138.setObjectName(u"valueLabel_138")
        self.valueLabel_138.setFont(font3)

        self.formLayout_3.setWidget(58, QFormLayout.FieldRole, self.valueLabel_138)

        self.valueLabel_139 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_139.setObjectName(u"valueLabel_139")
        self.valueLabel_139.setFont(font3)

        self.formLayout_3.setWidget(59, QFormLayout.FieldRole, self.valueLabel_139)

        self.valueLabel_140 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_140.setObjectName(u"valueLabel_140")
        self.valueLabel_140.setFont(font3)

        self.formLayout_3.setWidget(60, QFormLayout.FieldRole, self.valueLabel_140)

        self.addrLabel_141 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_141.setObjectName(u"addrLabel_141")
        self.addrLabel_141.setFont(font3)

        self.formLayout_3.setWidget(61, QFormLayout.LabelRole, self.addrLabel_141)

        self.addrLabel_142 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_142.setObjectName(u"addrLabel_142")
        self.addrLabel_142.setFont(font3)

        self.formLayout_3.setWidget(62, QFormLayout.LabelRole, self.addrLabel_142)

        self.addrLabel_143 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_143.setObjectName(u"addrLabel_143")
        self.addrLabel_143.setFont(font3)

        self.formLayout_3.setWidget(63, QFormLayout.LabelRole, self.addrLabel_143)

        self.addrLabel_144 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_144.setObjectName(u"addrLabel_144")
        self.addrLabel_144.setFont(font3)

        self.formLayout_3.setWidget(64, QFormLayout.LabelRole, self.addrLabel_144)

        self.addrLabel_145 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_145.setObjectName(u"addrLabel_145")
        self.addrLabel_145.setFont(font3)

        self.formLayout_3.setWidget(65, QFormLayout.LabelRole, self.addrLabel_145)

        self.addrLabel_146 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_146.setObjectName(u"addrLabel_146")
        self.addrLabel_146.setFont(font3)

        self.formLayout_3.setWidget(66, QFormLayout.LabelRole, self.addrLabel_146)

        self.addrLabel_147 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_147.setObjectName(u"addrLabel_147")
        self.addrLabel_147.setFont(font3)

        self.formLayout_3.setWidget(67, QFormLayout.LabelRole, self.addrLabel_147)

        self.addrLabel_148 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_148.setObjectName(u"addrLabel_148")
        self.addrLabel_148.setFont(font3)

        self.formLayout_3.setWidget(68, QFormLayout.LabelRole, self.addrLabel_148)

        self.addrLabel_149 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_149.setObjectName(u"addrLabel_149")
        self.addrLabel_149.setFont(font3)

        self.formLayout_3.setWidget(69, QFormLayout.LabelRole, self.addrLabel_149)

        self.addrLabel_150 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_150.setObjectName(u"addrLabel_150")
        self.addrLabel_150.setFont(font3)

        self.formLayout_3.setWidget(70, QFormLayout.LabelRole, self.addrLabel_150)

        self.valueLabel_141 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_141.setObjectName(u"valueLabel_141")
        self.valueLabel_141.setFont(font3)

        self.formLayout_3.setWidget(61, QFormLayout.FieldRole, self.valueLabel_141)

        self.valueLabel_142 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_142.setObjectName(u"valueLabel_142")
        self.valueLabel_142.setFont(font3)

        self.formLayout_3.setWidget(62, QFormLayout.FieldRole, self.valueLabel_142)

        self.valueLabel_143 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_143.setObjectName(u"valueLabel_143")
        self.valueLabel_143.setFont(font3)

        self.formLayout_3.setWidget(63, QFormLayout.FieldRole, self.valueLabel_143)

        self.valueLabel_144 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_144.setObjectName(u"valueLabel_144")
        self.valueLabel_144.setFont(font3)

        self.formLayout_3.setWidget(64, QFormLayout.FieldRole, self.valueLabel_144)

        self.valueLabel_145 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_145.setObjectName(u"valueLabel_145")
        self.valueLabel_145.setFont(font3)

        self.formLayout_3.setWidget(65, QFormLayout.FieldRole, self.valueLabel_145)

        self.valueLabel_146 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_146.setObjectName(u"valueLabel_146")
        self.valueLabel_146.setFont(font3)

        self.formLayout_3.setWidget(66, QFormLayout.FieldRole, self.valueLabel_146)

        self.valueLabel_147 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_147.setObjectName(u"valueLabel_147")
        self.valueLabel_147.setFont(font3)

        self.formLayout_3.setWidget(67, QFormLayout.FieldRole, self.valueLabel_147)

        self.valueLabel_148 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_148.setObjectName(u"valueLabel_148")
        self.valueLabel_148.setFont(font3)

        self.formLayout_3.setWidget(68, QFormLayout.FieldRole, self.valueLabel_148)

        self.valueLabel_149 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_149.setObjectName(u"valueLabel_149")
        self.valueLabel_149.setFont(font3)

        self.formLayout_3.setWidget(69, QFormLayout.FieldRole, self.valueLabel_149)

        self.valueLabel_150 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_150.setObjectName(u"valueLabel_150")
        self.valueLabel_150.setFont(font3)

        self.formLayout_3.setWidget(70, QFormLayout.FieldRole, self.valueLabel_150)

        self.addrLabel_151 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_151.setObjectName(u"addrLabel_151")
        self.addrLabel_151.setFont(font3)

        self.formLayout_3.setWidget(71, QFormLayout.LabelRole, self.addrLabel_151)

        self.addrLabel_152 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_152.setObjectName(u"addrLabel_152")
        self.addrLabel_152.setFont(font3)

        self.formLayout_3.setWidget(72, QFormLayout.LabelRole, self.addrLabel_152)

        self.addrLabel_153 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_153.setObjectName(u"addrLabel_153")
        self.addrLabel_153.setFont(font3)

        self.formLayout_3.setWidget(73, QFormLayout.LabelRole, self.addrLabel_153)

        self.addrLabel_154 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_154.setObjectName(u"addrLabel_154")
        self.addrLabel_154.setFont(font3)

        self.formLayout_3.setWidget(74, QFormLayout.LabelRole, self.addrLabel_154)

        self.addrLabel_155 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_155.setObjectName(u"addrLabel_155")
        self.addrLabel_155.setFont(font3)

        self.formLayout_3.setWidget(75, QFormLayout.LabelRole, self.addrLabel_155)

        self.addrLabel_156 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_156.setObjectName(u"addrLabel_156")
        self.addrLabel_156.setFont(font3)

        self.formLayout_3.setWidget(76, QFormLayout.LabelRole, self.addrLabel_156)

        self.addrLabel_157 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_157.setObjectName(u"addrLabel_157")
        self.addrLabel_157.setFont(font3)

        self.formLayout_3.setWidget(77, QFormLayout.LabelRole, self.addrLabel_157)

        self.addrLabel_158 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_158.setObjectName(u"addrLabel_158")
        self.addrLabel_158.setFont(font3)

        self.formLayout_3.setWidget(78, QFormLayout.LabelRole, self.addrLabel_158)

        self.addrLabel_159 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_159.setObjectName(u"addrLabel_159")
        self.addrLabel_159.setFont(font3)

        self.formLayout_3.setWidget(79, QFormLayout.LabelRole, self.addrLabel_159)

        self.addrLabel_160 = QLabel(self.scrollAreaWidgetContents_3)
        self.addrLabel_160.setObjectName(u"addrLabel_160")
        self.addrLabel_160.setFont(font3)

        self.formLayout_3.setWidget(80, QFormLayout.LabelRole, self.addrLabel_160)

        self.valueLabel_151 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_151.setObjectName(u"valueLabel_151")
        self.valueLabel_151.setFont(font3)

        self.formLayout_3.setWidget(71, QFormLayout.FieldRole, self.valueLabel_151)

        self.valueLabel_152 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_152.setObjectName(u"valueLabel_152")
        self.valueLabel_152.setFont(font3)

        self.formLayout_3.setWidget(72, QFormLayout.FieldRole, self.valueLabel_152)

        self.valueLabel_153 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_153.setObjectName(u"valueLabel_153")
        self.valueLabel_153.setFont(font3)

        self.formLayout_3.setWidget(73, QFormLayout.FieldRole, self.valueLabel_153)

        self.valueLabel_154 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_154.setObjectName(u"valueLabel_154")
        self.valueLabel_154.setFont(font3)

        self.formLayout_3.setWidget(74, QFormLayout.FieldRole, self.valueLabel_154)

        self.valueLabel_155 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_155.setObjectName(u"valueLabel_155")
        self.valueLabel_155.setFont(font3)

        self.formLayout_3.setWidget(75, QFormLayout.FieldRole, self.valueLabel_155)

        self.valueLabel_156 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_156.setObjectName(u"valueLabel_156")
        self.valueLabel_156.setFont(font3)

        self.formLayout_3.setWidget(76, QFormLayout.FieldRole, self.valueLabel_156)

        self.valueLabel_157 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_157.setObjectName(u"valueLabel_157")
        self.valueLabel_157.setFont(font3)

        self.formLayout_3.setWidget(77, QFormLayout.FieldRole, self.valueLabel_157)

        self.valueLabel_158 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_158.setObjectName(u"valueLabel_158")
        self.valueLabel_158.setFont(font3)

        self.formLayout_3.setWidget(78, QFormLayout.FieldRole, self.valueLabel_158)

        self.valueLabel_159 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_159.setObjectName(u"valueLabel_159")
        self.valueLabel_159.setFont(font3)

        self.formLayout_3.setWidget(79, QFormLayout.FieldRole, self.valueLabel_159)

        self.valueLabel_160 = QLabel(self.scrollAreaWidgetContents_3)
        self.valueLabel_160.setObjectName(u"valueLabel_160")
        self.valueLabel_160.setFont(font3)

        self.formLayout_3.setWidget(80, QFormLayout.FieldRole, self.valueLabel_160)

        self.memoriaArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.memoriaMainLabel_2 = QLabel(self.centralwidget)
        self.memoriaMainLabel_2.setObjectName(u"memoriaMainLabel_2")
        self.memoriaMainLabel_2.setGeometry(QRect(650, 60, 71, 31))
        self.memoriaMainLabel_2.setFont(font4)
        SegmentadoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SegmentadoWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 811, 22))
        SegmentadoWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SegmentadoWindow)
        self.statusbar.setObjectName(u"statusbar")
        SegmentadoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SegmentadoWindow)

        QMetaObject.connectSlotsByName(SegmentadoWindow)
    # setupUi

    def retranslateUi(self, SegmentadoWindow):
        SegmentadoWindow.setWindowTitle(QCoreApplication.translate("SegmentadoWindow", u"SegmentadoWindow", None))
        self.label.setText(QCoreApplication.translate("SegmentadoWindow", u"Numero de ciclo", None))
        self.pcLabel.setText(QCoreApplication.translate("SegmentadoWindow", u"pcLabel", None))
        self.pcNumberLabel.setText(QCoreApplication.translate("SegmentadoWindow", u"NUM PC", None))
        self.rxMainLabel.setText(QCoreApplication.translate("SegmentadoWindow", u"RX", None))
        self.valueRegistrosMainLabel.setText(QCoreApplication.translate("SegmentadoWindow", u"Value", None))
        self.rxLabel2.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel3.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_2.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel4.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_3.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel5.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_4.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel6.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_5.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_10.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_9.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_8.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_7.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_6.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel7.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel8.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel9.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel10.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel11.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel12.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_11.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel13.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_12.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_22.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_21.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_20.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_19.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_18.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_17.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_16.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_15.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_14.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_13.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel14.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel15.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel16.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel17.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel18.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel19.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel20.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel21.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel22.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel23.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel24.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_23.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel25.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel30.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel29.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel28.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel27.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel26.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_24.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_25.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_26.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_27.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_28.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_29.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_30.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_31.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel31.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel32.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.rxLabel33.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueMemLabel_32.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.registroMainLabel.setText(QCoreApplication.translate("SegmentadoWindow", u"Registros", None))
        self.rxMainLabel_3.setText(QCoreApplication.translate("SegmentadoWindow", u"addr", None))
        self.valueRegistrosLabel_3.setText(QCoreApplication.translate("SegmentadoWindow", u"Value", None))
        self.addrLabel.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_2.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_2.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_3.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_3.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_4.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_4.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_5.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_5.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_6.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_6.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_7.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_7.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_8.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_8.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_9.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_9.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_10.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_10.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_16.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_11.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_18.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_12.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_14.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_13.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_12.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_14.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_11.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_15.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_15.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_16.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_17.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_17.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_13.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_18.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_19.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_19.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_20.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_20.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_21.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_21.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_22.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_23.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_31.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_28.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_26.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_24.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_27.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_30.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_25.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_29.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_22.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_23.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_24.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_25.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_26.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_27.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_28.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_29.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_30.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_31.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_32.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_33.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_34.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_35.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_36.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_37.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_38.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_39.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_40.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_32.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_33.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_34.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_35.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_36.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_37.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_38.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_39.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_40.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_41.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_42.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_43.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_44.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_45.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_46.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_47.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_48.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_49.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_50.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_41.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_42.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_43.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_44.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_45.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_46.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_47.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_48.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_49.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_50.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_51.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_52.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_53.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_54.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_55.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_56.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_57.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_58.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_59.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_60.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_51.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_52.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_53.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_54.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_55.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_56.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_57.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_58.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_59.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_60.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_61.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_62.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_63.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_64.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_65.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_66.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_67.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_68.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_69.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_70.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_61.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_62.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_63.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_64.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_65.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_66.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_67.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_68.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_69.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_70.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_71.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_72.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_73.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_74.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_75.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_76.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_77.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_78.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_79.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_80.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_71.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_72.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_73.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_74.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_75.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_76.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_77.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_78.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_79.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_80.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.memoriaMainLabel.setText(QCoreApplication.translate("SegmentadoWindow", u"Memoria", None))
        self.rxMainLabel_4.setText(QCoreApplication.translate("SegmentadoWindow", u"addr", None))
        self.valueRegistrosLabel_4.setText(QCoreApplication.translate("SegmentadoWindow", u"Value", None))
        self.addrLabel_81.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_81.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_82.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_82.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_83.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_83.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_84.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_84.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_85.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_85.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_86.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_86.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_87.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_87.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_88.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_88.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_89.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_89.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_90.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_90.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_91.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_91.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_92.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_92.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_93.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_93.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_94.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_94.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_95.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_95.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_96.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_96.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_97.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_97.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_98.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_98.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_99.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_99.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_100.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_100.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_101.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_101.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_102.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_103.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_104.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_105.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_106.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_107.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_108.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_109.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_110.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_111.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_102.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_103.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_104.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_105.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_106.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_107.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_108.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_109.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_110.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_111.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_112.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_113.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_114.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_115.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_116.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_117.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_118.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_119.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_120.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_112.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_113.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_114.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_115.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_116.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_117.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_118.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_119.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_120.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_121.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_122.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_123.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_124.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_125.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_126.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_127.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_128.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_129.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_130.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_121.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_122.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_123.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_124.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_125.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_126.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_127.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_128.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_129.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_130.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_131.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_132.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_133.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_134.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_135.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_136.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_137.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_138.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_139.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_140.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_131.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_132.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_133.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_134.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_135.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_136.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_137.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_138.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_139.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_140.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_141.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_142.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_143.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_144.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_145.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_146.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_147.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_148.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_149.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_150.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_141.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_142.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_143.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_144.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_145.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_146.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_147.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_148.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_149.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_150.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_151.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_152.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_153.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_154.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_155.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_156.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_157.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_158.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_159.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.addrLabel_160.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_151.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_152.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_153.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_154.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_155.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_156.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_157.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_158.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_159.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.valueLabel_160.setText(QCoreApplication.translate("SegmentadoWindow", u"TextLabel", None))
        self.memoriaMainLabel_2.setText(QCoreApplication.translate("SegmentadoWindow", u"Memoria", None))
    # retranslateUi

