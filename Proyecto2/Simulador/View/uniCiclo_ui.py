# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UnicicloWindowGUIYKIQHY.ui'
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

class Ui_unicicloWindow(object):
    def setupUi(self, unicicloWindow):
        if not unicicloWindow.objectName():
            unicicloWindow.setObjectName(u"unicicloWindow")
        unicicloWindow.resize(863, 661)
        self.centralwidget = QWidget(unicicloWindow)
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
        self.pcLabel.setGeometry(QRect(20, 100, 81, 31))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.pcLabel.setFont(font1)
        self.pcNumberLabel = QLabel(self.centralwidget)
        self.pcNumberLabel.setObjectName(u"pcNumberLabel")
        self.pcNumberLabel.setGeometry(QRect(50, 130, 71, 41))
        font2 = QFont()
        font2.setPointSize(11)
        self.pcNumberLabel.setFont(font2)
        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(50, 60, 64, 23))
        self.registroMainLabel = QLabel(self.centralwidget)
        self.registroMainLabel.setObjectName(u"registroMainLabel")
        self.registroMainLabel.setGeometry(QRect(330, 60, 71, 31))
        font3 = QFont()
        font3.setPointSize(12)
        self.registroMainLabel.setFont(font3)
        self.registroArea = QScrollArea(self.centralwidget)
        self.registroArea.setObjectName(u"registroArea")
        self.registroArea.setGeometry(QRect(290, 90, 161, 331))
        self.registroArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 142, 742))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName(u"formLayout")
        self.rxMainLabel_2 = QLabel(self.scrollAreaWidgetContents)
        self.rxMainLabel_2.setObjectName(u"rxMainLabel_2")
        self.rxMainLabel_2.setFont(font2)
        self.rxMainLabel_2.setTextFormat(Qt.AutoText)
        self.rxMainLabel_2.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.rxMainLabel_2)

        self.valueRegistrosLabel_2 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegistrosLabel_2.setObjectName(u"valueRegistrosLabel_2")
        self.valueRegistrosLabel_2.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.valueRegistrosLabel_2)

        self.rxLabel = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel.setObjectName(u"rxLabel")
        font4 = QFont()
        font4.setPointSize(9)
        self.rxLabel.setFont(font4)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.rxLabel)

        self.valueRegLabel = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel.setObjectName(u"valueRegLabel")
        self.valueRegLabel.setFont(font4)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.valueRegLabel)

        self.rxLabel_2 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_2.setObjectName(u"rxLabel_2")
        self.rxLabel_2.setFont(font4)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.rxLabel_2)

        self.valueRegLabel_2 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_2.setObjectName(u"valueRegLabel_2")
        self.valueRegLabel_2.setFont(font4)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.valueRegLabel_2)

        self.rxLabel_3 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_3.setObjectName(u"rxLabel_3")
        self.rxLabel_3.setFont(font4)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.rxLabel_3)

        self.valueRegLabel_3 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_3.setObjectName(u"valueRegLabel_3")
        self.valueRegLabel_3.setFont(font4)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.valueRegLabel_3)

        self.rxLabel_4 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_4.setObjectName(u"rxLabel_4")
        self.rxLabel_4.setFont(font4)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.rxLabel_4)

        self.valueRegLabel_4 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_4.setObjectName(u"valueRegLabel_4")
        self.valueRegLabel_4.setFont(font4)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.valueRegLabel_4)

        self.rxLabel_5 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_5.setObjectName(u"rxLabel_5")
        self.rxLabel_5.setFont(font4)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.rxLabel_5)

        self.valueRegLabel_5 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_5.setObjectName(u"valueRegLabel_5")
        self.valueRegLabel_5.setFont(font4)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.valueRegLabel_5)

        self.valueRegLabel_10 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_10.setObjectName(u"valueRegLabel_10")
        self.valueRegLabel_10.setFont(font4)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.valueRegLabel_10)

        self.valueRegLabel_9 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_9.setObjectName(u"valueRegLabel_9")
        self.valueRegLabel_9.setFont(font4)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.valueRegLabel_9)

        self.valueRegLabel_8 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_8.setObjectName(u"valueRegLabel_8")
        self.valueRegLabel_8.setFont(font4)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.valueRegLabel_8)

        self.valueRegLabel_7 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_7.setObjectName(u"valueRegLabel_7")
        self.valueRegLabel_7.setFont(font4)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.valueRegLabel_7)

        self.valueRegLabel_6 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_6.setObjectName(u"valueRegLabel_6")
        self.valueRegLabel_6.setFont(font4)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.valueRegLabel_6)

        self.rxLabel_6 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_6.setObjectName(u"rxLabel_6")
        self.rxLabel_6.setFont(font4)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.rxLabel_6)

        self.rxLabel_7 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_7.setObjectName(u"rxLabel_7")
        self.rxLabel_7.setFont(font4)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.rxLabel_7)

        self.rxLabel_8 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_8.setObjectName(u"rxLabel_8")
        self.rxLabel_8.setFont(font4)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.rxLabel_8)

        self.rxLabel_9 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_9.setObjectName(u"rxLabel_9")
        self.rxLabel_9.setFont(font4)

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.rxLabel_9)

        self.rxLabel_10 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_10.setObjectName(u"rxLabel_10")
        self.rxLabel_10.setFont(font4)

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.rxLabel_10)

        self.rxLabel_11 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_11.setObjectName(u"rxLabel_11")
        self.rxLabel_11.setFont(font4)

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.rxLabel_11)

        self.valueRegLabel_11 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_11.setObjectName(u"valueRegLabel_11")
        self.valueRegLabel_11.setFont(font4)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.valueRegLabel_11)

        self.rxLabel_12 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_12.setObjectName(u"rxLabel_12")
        self.rxLabel_12.setFont(font4)

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.rxLabel_12)

        self.valueRegLabel_12 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_12.setObjectName(u"valueRegLabel_12")
        self.valueRegLabel_12.setFont(font4)

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.valueRegLabel_12)

        self.valueRegLabel_22 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_22.setObjectName(u"valueRegLabel_22")
        self.valueRegLabel_22.setFont(font4)

        self.formLayout.setWidget(22, QFormLayout.FieldRole, self.valueRegLabel_22)

        self.valueRegLabel_21 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_21.setObjectName(u"valueRegLabel_21")
        self.valueRegLabel_21.setFont(font4)

        self.formLayout.setWidget(21, QFormLayout.FieldRole, self.valueRegLabel_21)

        self.valueRegLabel_20 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_20.setObjectName(u"valueRegLabel_20")
        self.valueRegLabel_20.setFont(font4)

        self.formLayout.setWidget(20, QFormLayout.FieldRole, self.valueRegLabel_20)

        self.valueRegLabel_19 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_19.setObjectName(u"valueRegLabel_19")
        self.valueRegLabel_19.setFont(font4)

        self.formLayout.setWidget(19, QFormLayout.FieldRole, self.valueRegLabel_19)

        self.valueRegLabel_18 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_18.setObjectName(u"valueRegLabel_18")
        self.valueRegLabel_18.setFont(font4)

        self.formLayout.setWidget(18, QFormLayout.FieldRole, self.valueRegLabel_18)

        self.valueRegLabel_17 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_17.setObjectName(u"valueRegLabel_17")
        self.valueRegLabel_17.setFont(font4)

        self.formLayout.setWidget(17, QFormLayout.FieldRole, self.valueRegLabel_17)

        self.valueRegLabel_16 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_16.setObjectName(u"valueRegLabel_16")
        self.valueRegLabel_16.setFont(font4)

        self.formLayout.setWidget(16, QFormLayout.FieldRole, self.valueRegLabel_16)

        self.valueRegLabel_15 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_15.setObjectName(u"valueRegLabel_15")
        self.valueRegLabel_15.setFont(font4)

        self.formLayout.setWidget(15, QFormLayout.FieldRole, self.valueRegLabel_15)

        self.valueRegLabel_14 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_14.setObjectName(u"valueRegLabel_14")
        self.valueRegLabel_14.setFont(font4)

        self.formLayout.setWidget(14, QFormLayout.FieldRole, self.valueRegLabel_14)

        self.valueRegLabel_13 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_13.setObjectName(u"valueRegLabel_13")
        self.valueRegLabel_13.setFont(font4)

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.valueRegLabel_13)

        self.rxLabel_13 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_13.setObjectName(u"rxLabel_13")
        self.rxLabel_13.setFont(font4)

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.rxLabel_13)

        self.rxLabel_14 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_14.setObjectName(u"rxLabel_14")
        self.rxLabel_14.setFont(font4)

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.rxLabel_14)

        self.rxLabel_15 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_15.setObjectName(u"rxLabel_15")
        self.rxLabel_15.setFont(font4)

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.rxLabel_15)

        self.rxLabel_16 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_16.setObjectName(u"rxLabel_16")
        self.rxLabel_16.setFont(font4)

        self.formLayout.setWidget(16, QFormLayout.LabelRole, self.rxLabel_16)

        self.rxLabel_17 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_17.setObjectName(u"rxLabel_17")
        self.rxLabel_17.setFont(font4)

        self.formLayout.setWidget(17, QFormLayout.LabelRole, self.rxLabel_17)

        self.rxLabel_18 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_18.setObjectName(u"rxLabel_18")
        self.rxLabel_18.setFont(font4)

        self.formLayout.setWidget(18, QFormLayout.LabelRole, self.rxLabel_18)

        self.rxLabel_19 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_19.setObjectName(u"rxLabel_19")
        self.rxLabel_19.setFont(font4)

        self.formLayout.setWidget(19, QFormLayout.LabelRole, self.rxLabel_19)

        self.rxLabel_20 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_20.setObjectName(u"rxLabel_20")
        self.rxLabel_20.setFont(font4)

        self.formLayout.setWidget(20, QFormLayout.LabelRole, self.rxLabel_20)

        self.rxLabel_21 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_21.setObjectName(u"rxLabel_21")
        self.rxLabel_21.setFont(font4)

        self.formLayout.setWidget(21, QFormLayout.LabelRole, self.rxLabel_21)

        self.rxLabel_22 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_22.setObjectName(u"rxLabel_22")
        self.rxLabel_22.setFont(font4)

        self.formLayout.setWidget(22, QFormLayout.LabelRole, self.rxLabel_22)

        self.rxLabel_23 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_23.setObjectName(u"rxLabel_23")
        self.rxLabel_23.setFont(font4)

        self.formLayout.setWidget(23, QFormLayout.LabelRole, self.rxLabel_23)

        self.rxLabel_24 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_24.setObjectName(u"rxLabel_24")
        self.rxLabel_24.setFont(font4)

        self.formLayout.setWidget(24, QFormLayout.LabelRole, self.rxLabel_24)

        self.rxLabel_25 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_25.setObjectName(u"rxLabel_25")
        self.rxLabel_25.setFont(font4)

        self.formLayout.setWidget(25, QFormLayout.LabelRole, self.rxLabel_25)

        self.rxLabel_26 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_26.setObjectName(u"rxLabel_26")
        self.rxLabel_26.setFont(font4)

        self.formLayout.setWidget(26, QFormLayout.LabelRole, self.rxLabel_26)

        self.rxLabel_27 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_27.setObjectName(u"rxLabel_27")
        self.rxLabel_27.setFont(font4)

        self.formLayout.setWidget(27, QFormLayout.LabelRole, self.rxLabel_27)

        self.rxLabel_28 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_28.setObjectName(u"rxLabel_28")
        self.rxLabel_28.setFont(font4)

        self.formLayout.setWidget(28, QFormLayout.LabelRole, self.rxLabel_28)

        self.rxLabel_29 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_29.setObjectName(u"rxLabel_29")
        self.rxLabel_29.setFont(font4)

        self.formLayout.setWidget(29, QFormLayout.LabelRole, self.rxLabel_29)

        self.rxLabel_30 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_30.setObjectName(u"rxLabel_30")
        self.rxLabel_30.setFont(font4)

        self.formLayout.setWidget(30, QFormLayout.LabelRole, self.rxLabel_30)

        self.rxLabel_31 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_31.setObjectName(u"rxLabel_31")
        self.rxLabel_31.setFont(font4)

        self.formLayout.setWidget(31, QFormLayout.LabelRole, self.rxLabel_31)

        self.rxLabel_32 = QLabel(self.scrollAreaWidgetContents)
        self.rxLabel_32.setObjectName(u"rxLabel_32")
        self.rxLabel_32.setFont(font4)

        self.formLayout.setWidget(32, QFormLayout.LabelRole, self.rxLabel_32)

        self.valueRegLabel_23 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_23.setObjectName(u"valueRegLabel_23")
        self.valueRegLabel_23.setFont(font4)

        self.formLayout.setWidget(23, QFormLayout.FieldRole, self.valueRegLabel_23)

        self.valueRegLabel_24 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_24.setObjectName(u"valueRegLabel_24")
        self.valueRegLabel_24.setFont(font4)

        self.formLayout.setWidget(24, QFormLayout.FieldRole, self.valueRegLabel_24)

        self.valueRegLabel_25 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_25.setObjectName(u"valueRegLabel_25")
        self.valueRegLabel_25.setFont(font4)

        self.formLayout.setWidget(25, QFormLayout.FieldRole, self.valueRegLabel_25)

        self.valueRegLabel_26 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_26.setObjectName(u"valueRegLabel_26")
        self.valueRegLabel_26.setFont(font4)

        self.formLayout.setWidget(26, QFormLayout.FieldRole, self.valueRegLabel_26)

        self.valueRegLabel_27 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_27.setObjectName(u"valueRegLabel_27")
        self.valueRegLabel_27.setFont(font4)

        self.formLayout.setWidget(27, QFormLayout.FieldRole, self.valueRegLabel_27)

        self.valueRegLabel_28 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_28.setObjectName(u"valueRegLabel_28")
        self.valueRegLabel_28.setFont(font4)

        self.formLayout.setWidget(28, QFormLayout.FieldRole, self.valueRegLabel_28)

        self.valueRegLabel_29 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_29.setObjectName(u"valueRegLabel_29")
        self.valueRegLabel_29.setFont(font4)

        self.formLayout.setWidget(29, QFormLayout.FieldRole, self.valueRegLabel_29)

        self.valueRegLabel_30 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_30.setObjectName(u"valueRegLabel_30")
        self.valueRegLabel_30.setFont(font4)

        self.formLayout.setWidget(30, QFormLayout.FieldRole, self.valueRegLabel_30)

        self.valueRegLabel_31 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_31.setObjectName(u"valueRegLabel_31")
        self.valueRegLabel_31.setFont(font4)

        self.formLayout.setWidget(31, QFormLayout.FieldRole, self.valueRegLabel_31)

        self.valueRegLabel_32 = QLabel(self.scrollAreaWidgetContents)
        self.valueRegLabel_32.setObjectName(u"valueRegLabel_32")
        self.valueRegLabel_32.setFont(font4)

        self.formLayout.setWidget(32, QFormLayout.FieldRole, self.valueRegLabel_32)

        self.registroArea.setWidget(self.scrollAreaWidgetContents)
        self.memoriaMainLabel = QLabel(self.centralwidget)
        self.memoriaMainLabel.setObjectName(u"memoriaMainLabel")
        self.memoriaMainLabel.setGeometry(QRect(640, 60, 71, 31))
        self.memoriaMainLabel.setFont(font3)
        self.memoriaArea = QScrollArea(self.centralwidget)
        self.memoriaArea.setObjectName(u"memoriaArea")
        self.memoriaArea.setGeometry(QRect(610, 90, 161, 331))
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
        self.addrLabel.setFont(font4)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.addrLabel)

        self.valueLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel.setObjectName(u"valueLabel")
        self.valueLabel.setFont(font4)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.valueLabel)

        self.addrLabel_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_2.setObjectName(u"addrLabel_2")
        self.addrLabel_2.setFont(font4)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.addrLabel_2)

        self.valueLabel_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_2.setObjectName(u"valueLabel_2")
        self.valueLabel_2.setFont(font4)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.valueLabel_2)

        self.addrLabel_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_3.setObjectName(u"addrLabel_3")
        self.addrLabel_3.setFont(font4)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.addrLabel_3)

        self.valueLabel_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_3.setObjectName(u"valueLabel_3")
        self.valueLabel_3.setFont(font4)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.valueLabel_3)

        self.addrLabel_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_4.setObjectName(u"addrLabel_4")
        self.addrLabel_4.setFont(font4)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.addrLabel_4)

        self.valueLabel_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_4.setObjectName(u"valueLabel_4")
        self.valueLabel_4.setFont(font4)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.valueLabel_4)

        self.addrLabel_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_5.setObjectName(u"addrLabel_5")
        self.addrLabel_5.setFont(font4)

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.addrLabel_5)

        self.valueLabel_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_5.setObjectName(u"valueLabel_5")
        self.valueLabel_5.setFont(font4)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.valueLabel_5)

        self.addrLabel_6 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_6.setObjectName(u"addrLabel_6")
        self.addrLabel_6.setFont(font4)

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.addrLabel_6)

        self.valueLabel_6 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_6.setObjectName(u"valueLabel_6")
        self.valueLabel_6.setFont(font4)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.valueLabel_6)

        self.addrLabel_7 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_7.setObjectName(u"addrLabel_7")
        self.addrLabel_7.setFont(font4)

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.addrLabel_7)

        self.valueLabel_7 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_7.setObjectName(u"valueLabel_7")
        self.valueLabel_7.setFont(font4)

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.valueLabel_7)

        self.addrLabel_8 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_8.setObjectName(u"addrLabel_8")
        self.addrLabel_8.setFont(font4)

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.addrLabel_8)

        self.valueLabel_8 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_8.setObjectName(u"valueLabel_8")
        self.valueLabel_8.setFont(font4)

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.valueLabel_8)

        self.addrLabel_9 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_9.setObjectName(u"addrLabel_9")
        self.addrLabel_9.setFont(font4)

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.addrLabel_9)

        self.valueLabel_9 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_9.setObjectName(u"valueLabel_9")
        self.valueLabel_9.setFont(font4)

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.valueLabel_9)

        self.addrLabel_10 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_10.setObjectName(u"addrLabel_10")
        self.addrLabel_10.setFont(font4)

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.addrLabel_10)

        self.valueLabel_10 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_10.setObjectName(u"valueLabel_10")
        self.valueLabel_10.setFont(font4)

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.valueLabel_10)

        self.addrLabel_16 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_16.setObjectName(u"addrLabel_16")
        self.addrLabel_16.setFont(font4)

        self.formLayout_2.setWidget(11, QFormLayout.LabelRole, self.addrLabel_16)

        self.valueLabel_11 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_11.setObjectName(u"valueLabel_11")
        self.valueLabel_11.setFont(font4)

        self.formLayout_2.setWidget(11, QFormLayout.FieldRole, self.valueLabel_11)

        self.addrLabel_18 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_18.setObjectName(u"addrLabel_18")
        self.addrLabel_18.setFont(font4)

        self.formLayout_2.setWidget(12, QFormLayout.LabelRole, self.addrLabel_18)

        self.valueLabel_12 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_12.setObjectName(u"valueLabel_12")
        self.valueLabel_12.setFont(font4)

        self.formLayout_2.setWidget(12, QFormLayout.FieldRole, self.valueLabel_12)

        self.addrLabel_14 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_14.setObjectName(u"addrLabel_14")
        self.addrLabel_14.setFont(font4)

        self.formLayout_2.setWidget(13, QFormLayout.LabelRole, self.addrLabel_14)

        self.valueLabel_13 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_13.setObjectName(u"valueLabel_13")
        self.valueLabel_13.setFont(font4)

        self.formLayout_2.setWidget(13, QFormLayout.FieldRole, self.valueLabel_13)

        self.addrLabel_12 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_12.setObjectName(u"addrLabel_12")
        self.addrLabel_12.setFont(font4)

        self.formLayout_2.setWidget(14, QFormLayout.LabelRole, self.addrLabel_12)

        self.valueLabel_14 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_14.setObjectName(u"valueLabel_14")
        self.valueLabel_14.setFont(font4)

        self.formLayout_2.setWidget(14, QFormLayout.FieldRole, self.valueLabel_14)

        self.addrLabel_11 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_11.setObjectName(u"addrLabel_11")
        self.addrLabel_11.setFont(font4)

        self.formLayout_2.setWidget(15, QFormLayout.LabelRole, self.addrLabel_11)

        self.valueLabel_15 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_15.setObjectName(u"valueLabel_15")
        self.valueLabel_15.setFont(font4)

        self.formLayout_2.setWidget(15, QFormLayout.FieldRole, self.valueLabel_15)

        self.addrLabel_15 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_15.setObjectName(u"addrLabel_15")
        self.addrLabel_15.setFont(font4)

        self.formLayout_2.setWidget(16, QFormLayout.LabelRole, self.addrLabel_15)

        self.valueLabel_16 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_16.setObjectName(u"valueLabel_16")
        self.valueLabel_16.setFont(font4)

        self.formLayout_2.setWidget(16, QFormLayout.FieldRole, self.valueLabel_16)

        self.addrLabel_17 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_17.setObjectName(u"addrLabel_17")
        self.addrLabel_17.setFont(font4)

        self.formLayout_2.setWidget(17, QFormLayout.LabelRole, self.addrLabel_17)

        self.valueLabel_17 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_17.setObjectName(u"valueLabel_17")
        self.valueLabel_17.setFont(font4)

        self.formLayout_2.setWidget(17, QFormLayout.FieldRole, self.valueLabel_17)

        self.addrLabel_13 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_13.setObjectName(u"addrLabel_13")
        self.addrLabel_13.setFont(font4)

        self.formLayout_2.setWidget(18, QFormLayout.LabelRole, self.addrLabel_13)

        self.valueLabel_18 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_18.setObjectName(u"valueLabel_18")
        self.valueLabel_18.setFont(font4)

        self.formLayout_2.setWidget(18, QFormLayout.FieldRole, self.valueLabel_18)

        self.addrLabel_19 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_19.setObjectName(u"addrLabel_19")
        self.addrLabel_19.setFont(font4)

        self.formLayout_2.setWidget(19, QFormLayout.LabelRole, self.addrLabel_19)

        self.valueLabel_19 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_19.setObjectName(u"valueLabel_19")
        self.valueLabel_19.setFont(font4)

        self.formLayout_2.setWidget(19, QFormLayout.FieldRole, self.valueLabel_19)

        self.addrLabel_20 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_20.setObjectName(u"addrLabel_20")
        self.addrLabel_20.setFont(font4)

        self.formLayout_2.setWidget(20, QFormLayout.LabelRole, self.addrLabel_20)

        self.valueLabel_20 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_20.setObjectName(u"valueLabel_20")
        self.valueLabel_20.setFont(font4)

        self.formLayout_2.setWidget(20, QFormLayout.FieldRole, self.valueLabel_20)

        self.addrLabel_21 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_21.setObjectName(u"addrLabel_21")
        self.addrLabel_21.setFont(font4)

        self.formLayout_2.setWidget(21, QFormLayout.LabelRole, self.addrLabel_21)

        self.valueLabel_21 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_21.setObjectName(u"valueLabel_21")
        self.valueLabel_21.setFont(font4)

        self.formLayout_2.setWidget(21, QFormLayout.FieldRole, self.valueLabel_21)

        self.valueLabel_22 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_22.setObjectName(u"valueLabel_22")
        self.valueLabel_22.setFont(font4)

        self.formLayout_2.setWidget(22, QFormLayout.FieldRole, self.valueLabel_22)

        self.valueLabel_23 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_23.setObjectName(u"valueLabel_23")
        self.valueLabel_23.setFont(font4)

        self.formLayout_2.setWidget(23, QFormLayout.FieldRole, self.valueLabel_23)

        self.valueLabel_31 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_31.setObjectName(u"valueLabel_31")
        self.valueLabel_31.setFont(font4)

        self.formLayout_2.setWidget(31, QFormLayout.FieldRole, self.valueLabel_31)

        self.valueLabel_28 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_28.setObjectName(u"valueLabel_28")
        self.valueLabel_28.setFont(font4)

        self.formLayout_2.setWidget(30, QFormLayout.FieldRole, self.valueLabel_28)

        self.valueLabel_26 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_26.setObjectName(u"valueLabel_26")
        self.valueLabel_26.setFont(font4)

        self.formLayout_2.setWidget(29, QFormLayout.FieldRole, self.valueLabel_26)

        self.valueLabel_24 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_24.setObjectName(u"valueLabel_24")
        self.valueLabel_24.setFont(font4)

        self.formLayout_2.setWidget(28, QFormLayout.FieldRole, self.valueLabel_24)

        self.valueLabel_27 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_27.setObjectName(u"valueLabel_27")
        self.valueLabel_27.setFont(font4)

        self.formLayout_2.setWidget(27, QFormLayout.FieldRole, self.valueLabel_27)

        self.valueLabel_30 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_30.setObjectName(u"valueLabel_30")
        self.valueLabel_30.setFont(font4)

        self.formLayout_2.setWidget(26, QFormLayout.FieldRole, self.valueLabel_30)

        self.valueLabel_25 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_25.setObjectName(u"valueLabel_25")
        self.valueLabel_25.setFont(font4)

        self.formLayout_2.setWidget(25, QFormLayout.FieldRole, self.valueLabel_25)

        self.valueLabel_29 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_29.setObjectName(u"valueLabel_29")
        self.valueLabel_29.setFont(font4)

        self.formLayout_2.setWidget(24, QFormLayout.FieldRole, self.valueLabel_29)

        self.addrLabel_22 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_22.setObjectName(u"addrLabel_22")
        self.addrLabel_22.setFont(font4)

        self.formLayout_2.setWidget(22, QFormLayout.LabelRole, self.addrLabel_22)

        self.addrLabel_23 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_23.setObjectName(u"addrLabel_23")
        self.addrLabel_23.setFont(font4)

        self.formLayout_2.setWidget(23, QFormLayout.LabelRole, self.addrLabel_23)

        self.addrLabel_24 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_24.setObjectName(u"addrLabel_24")
        self.addrLabel_24.setFont(font4)

        self.formLayout_2.setWidget(24, QFormLayout.LabelRole, self.addrLabel_24)

        self.addrLabel_25 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_25.setObjectName(u"addrLabel_25")
        self.addrLabel_25.setFont(font4)

        self.formLayout_2.setWidget(25, QFormLayout.LabelRole, self.addrLabel_25)

        self.addrLabel_26 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_26.setObjectName(u"addrLabel_26")
        self.addrLabel_26.setFont(font4)

        self.formLayout_2.setWidget(26, QFormLayout.LabelRole, self.addrLabel_26)

        self.addrLabel_27 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_27.setObjectName(u"addrLabel_27")
        self.addrLabel_27.setFont(font4)

        self.formLayout_2.setWidget(27, QFormLayout.LabelRole, self.addrLabel_27)

        self.addrLabel_28 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_28.setObjectName(u"addrLabel_28")
        self.addrLabel_28.setFont(font4)

        self.formLayout_2.setWidget(28, QFormLayout.LabelRole, self.addrLabel_28)

        self.addrLabel_29 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_29.setObjectName(u"addrLabel_29")
        self.addrLabel_29.setFont(font4)

        self.formLayout_2.setWidget(29, QFormLayout.LabelRole, self.addrLabel_29)

        self.addrLabel_30 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_30.setObjectName(u"addrLabel_30")
        self.addrLabel_30.setFont(font4)

        self.formLayout_2.setWidget(30, QFormLayout.LabelRole, self.addrLabel_30)

        self.addrLabel_31 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_31.setObjectName(u"addrLabel_31")
        self.addrLabel_31.setFont(font4)

        self.formLayout_2.setWidget(31, QFormLayout.LabelRole, self.addrLabel_31)

        self.addrLabel_32 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_32.setObjectName(u"addrLabel_32")
        self.addrLabel_32.setFont(font4)

        self.formLayout_2.setWidget(32, QFormLayout.LabelRole, self.addrLabel_32)

        self.addrLabel_33 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_33.setObjectName(u"addrLabel_33")
        self.addrLabel_33.setFont(font4)

        self.formLayout_2.setWidget(33, QFormLayout.LabelRole, self.addrLabel_33)

        self.addrLabel_34 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_34.setObjectName(u"addrLabel_34")
        self.addrLabel_34.setFont(font4)

        self.formLayout_2.setWidget(34, QFormLayout.LabelRole, self.addrLabel_34)

        self.addrLabel_35 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_35.setObjectName(u"addrLabel_35")
        self.addrLabel_35.setFont(font4)

        self.formLayout_2.setWidget(35, QFormLayout.LabelRole, self.addrLabel_35)

        self.addrLabel_36 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_36.setObjectName(u"addrLabel_36")
        self.addrLabel_36.setFont(font4)

        self.formLayout_2.setWidget(36, QFormLayout.LabelRole, self.addrLabel_36)

        self.addrLabel_37 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_37.setObjectName(u"addrLabel_37")
        self.addrLabel_37.setFont(font4)

        self.formLayout_2.setWidget(37, QFormLayout.LabelRole, self.addrLabel_37)

        self.addrLabel_38 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_38.setObjectName(u"addrLabel_38")
        self.addrLabel_38.setFont(font4)

        self.formLayout_2.setWidget(38, QFormLayout.LabelRole, self.addrLabel_38)

        self.addrLabel_39 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_39.setObjectName(u"addrLabel_39")
        self.addrLabel_39.setFont(font4)

        self.formLayout_2.setWidget(39, QFormLayout.LabelRole, self.addrLabel_39)

        self.addrLabel_40 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_40.setObjectName(u"addrLabel_40")
        self.addrLabel_40.setFont(font4)

        self.formLayout_2.setWidget(40, QFormLayout.LabelRole, self.addrLabel_40)

        self.valueLabel_32 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_32.setObjectName(u"valueLabel_32")
        self.valueLabel_32.setFont(font4)

        self.formLayout_2.setWidget(32, QFormLayout.FieldRole, self.valueLabel_32)

        self.valueLabel_33 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_33.setObjectName(u"valueLabel_33")
        self.valueLabel_33.setFont(font4)

        self.formLayout_2.setWidget(33, QFormLayout.FieldRole, self.valueLabel_33)

        self.valueLabel_34 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_34.setObjectName(u"valueLabel_34")
        self.valueLabel_34.setFont(font4)

        self.formLayout_2.setWidget(34, QFormLayout.FieldRole, self.valueLabel_34)

        self.valueLabel_35 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_35.setObjectName(u"valueLabel_35")
        self.valueLabel_35.setFont(font4)

        self.formLayout_2.setWidget(35, QFormLayout.FieldRole, self.valueLabel_35)

        self.valueLabel_36 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_36.setObjectName(u"valueLabel_36")
        self.valueLabel_36.setFont(font4)

        self.formLayout_2.setWidget(36, QFormLayout.FieldRole, self.valueLabel_36)

        self.valueLabel_37 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_37.setObjectName(u"valueLabel_37")
        self.valueLabel_37.setFont(font4)

        self.formLayout_2.setWidget(37, QFormLayout.FieldRole, self.valueLabel_37)

        self.valueLabel_38 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_38.setObjectName(u"valueLabel_38")
        self.valueLabel_38.setFont(font4)

        self.formLayout_2.setWidget(38, QFormLayout.FieldRole, self.valueLabel_38)

        self.valueLabel_39 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_39.setObjectName(u"valueLabel_39")
        self.valueLabel_39.setFont(font4)

        self.formLayout_2.setWidget(39, QFormLayout.FieldRole, self.valueLabel_39)

        self.valueLabel_40 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_40.setObjectName(u"valueLabel_40")
        self.valueLabel_40.setFont(font4)

        self.formLayout_2.setWidget(40, QFormLayout.FieldRole, self.valueLabel_40)

        self.addrLabel_41 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_41.setObjectName(u"addrLabel_41")
        self.addrLabel_41.setFont(font4)

        self.formLayout_2.setWidget(41, QFormLayout.LabelRole, self.addrLabel_41)

        self.addrLabel_42 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_42.setObjectName(u"addrLabel_42")
        self.addrLabel_42.setFont(font4)

        self.formLayout_2.setWidget(42, QFormLayout.LabelRole, self.addrLabel_42)

        self.addrLabel_43 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_43.setObjectName(u"addrLabel_43")
        self.addrLabel_43.setFont(font4)

        self.formLayout_2.setWidget(43, QFormLayout.LabelRole, self.addrLabel_43)

        self.addrLabel_44 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_44.setObjectName(u"addrLabel_44")
        self.addrLabel_44.setFont(font4)

        self.formLayout_2.setWidget(44, QFormLayout.LabelRole, self.addrLabel_44)

        self.addrLabel_45 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_45.setObjectName(u"addrLabel_45")
        self.addrLabel_45.setFont(font4)

        self.formLayout_2.setWidget(45, QFormLayout.LabelRole, self.addrLabel_45)

        self.addrLabel_46 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_46.setObjectName(u"addrLabel_46")
        self.addrLabel_46.setFont(font4)

        self.formLayout_2.setWidget(46, QFormLayout.LabelRole, self.addrLabel_46)

        self.addrLabel_47 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_47.setObjectName(u"addrLabel_47")
        self.addrLabel_47.setFont(font4)

        self.formLayout_2.setWidget(47, QFormLayout.LabelRole, self.addrLabel_47)

        self.addrLabel_48 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_48.setObjectName(u"addrLabel_48")
        self.addrLabel_48.setFont(font4)

        self.formLayout_2.setWidget(48, QFormLayout.LabelRole, self.addrLabel_48)

        self.addrLabel_49 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_49.setObjectName(u"addrLabel_49")
        self.addrLabel_49.setFont(font4)

        self.formLayout_2.setWidget(49, QFormLayout.LabelRole, self.addrLabel_49)

        self.addrLabel_50 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_50.setObjectName(u"addrLabel_50")
        self.addrLabel_50.setFont(font4)

        self.formLayout_2.setWidget(50, QFormLayout.LabelRole, self.addrLabel_50)

        self.valueLabel_41 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_41.setObjectName(u"valueLabel_41")
        self.valueLabel_41.setFont(font4)

        self.formLayout_2.setWidget(41, QFormLayout.FieldRole, self.valueLabel_41)

        self.valueLabel_42 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_42.setObjectName(u"valueLabel_42")
        self.valueLabel_42.setFont(font4)

        self.formLayout_2.setWidget(42, QFormLayout.FieldRole, self.valueLabel_42)

        self.valueLabel_43 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_43.setObjectName(u"valueLabel_43")
        self.valueLabel_43.setFont(font4)

        self.formLayout_2.setWidget(43, QFormLayout.FieldRole, self.valueLabel_43)

        self.valueLabel_44 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_44.setObjectName(u"valueLabel_44")
        self.valueLabel_44.setFont(font4)

        self.formLayout_2.setWidget(44, QFormLayout.FieldRole, self.valueLabel_44)

        self.valueLabel_45 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_45.setObjectName(u"valueLabel_45")
        self.valueLabel_45.setFont(font4)

        self.formLayout_2.setWidget(45, QFormLayout.FieldRole, self.valueLabel_45)

        self.valueLabel_46 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_46.setObjectName(u"valueLabel_46")
        self.valueLabel_46.setFont(font4)

        self.formLayout_2.setWidget(46, QFormLayout.FieldRole, self.valueLabel_46)

        self.valueLabel_47 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_47.setObjectName(u"valueLabel_47")
        self.valueLabel_47.setFont(font4)

        self.formLayout_2.setWidget(47, QFormLayout.FieldRole, self.valueLabel_47)

        self.valueLabel_48 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_48.setObjectName(u"valueLabel_48")
        self.valueLabel_48.setFont(font4)

        self.formLayout_2.setWidget(48, QFormLayout.FieldRole, self.valueLabel_48)

        self.valueLabel_49 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_49.setObjectName(u"valueLabel_49")
        self.valueLabel_49.setFont(font4)

        self.formLayout_2.setWidget(49, QFormLayout.FieldRole, self.valueLabel_49)

        self.valueLabel_50 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_50.setObjectName(u"valueLabel_50")
        self.valueLabel_50.setFont(font4)

        self.formLayout_2.setWidget(50, QFormLayout.FieldRole, self.valueLabel_50)

        self.addrLabel_51 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_51.setObjectName(u"addrLabel_51")
        self.addrLabel_51.setFont(font4)

        self.formLayout_2.setWidget(51, QFormLayout.LabelRole, self.addrLabel_51)

        self.addrLabel_52 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_52.setObjectName(u"addrLabel_52")
        self.addrLabel_52.setFont(font4)

        self.formLayout_2.setWidget(52, QFormLayout.LabelRole, self.addrLabel_52)

        self.addrLabel_53 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_53.setObjectName(u"addrLabel_53")
        self.addrLabel_53.setFont(font4)

        self.formLayout_2.setWidget(53, QFormLayout.LabelRole, self.addrLabel_53)

        self.addrLabel_54 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_54.setObjectName(u"addrLabel_54")
        self.addrLabel_54.setFont(font4)

        self.formLayout_2.setWidget(54, QFormLayout.LabelRole, self.addrLabel_54)

        self.addrLabel_55 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_55.setObjectName(u"addrLabel_55")
        self.addrLabel_55.setFont(font4)

        self.formLayout_2.setWidget(55, QFormLayout.LabelRole, self.addrLabel_55)

        self.addrLabel_56 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_56.setObjectName(u"addrLabel_56")
        self.addrLabel_56.setFont(font4)

        self.formLayout_2.setWidget(56, QFormLayout.LabelRole, self.addrLabel_56)

        self.addrLabel_57 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_57.setObjectName(u"addrLabel_57")
        self.addrLabel_57.setFont(font4)

        self.formLayout_2.setWidget(57, QFormLayout.LabelRole, self.addrLabel_57)

        self.addrLabel_58 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_58.setObjectName(u"addrLabel_58")
        self.addrLabel_58.setFont(font4)

        self.formLayout_2.setWidget(58, QFormLayout.LabelRole, self.addrLabel_58)

        self.addrLabel_59 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_59.setObjectName(u"addrLabel_59")
        self.addrLabel_59.setFont(font4)

        self.formLayout_2.setWidget(59, QFormLayout.LabelRole, self.addrLabel_59)

        self.addrLabel_60 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_60.setObjectName(u"addrLabel_60")
        self.addrLabel_60.setFont(font4)

        self.formLayout_2.setWidget(60, QFormLayout.LabelRole, self.addrLabel_60)

        self.valueLabel_51 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_51.setObjectName(u"valueLabel_51")
        self.valueLabel_51.setFont(font4)

        self.formLayout_2.setWidget(51, QFormLayout.FieldRole, self.valueLabel_51)

        self.valueLabel_52 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_52.setObjectName(u"valueLabel_52")
        self.valueLabel_52.setFont(font4)

        self.formLayout_2.setWidget(52, QFormLayout.FieldRole, self.valueLabel_52)

        self.valueLabel_53 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_53.setObjectName(u"valueLabel_53")
        self.valueLabel_53.setFont(font4)

        self.formLayout_2.setWidget(53, QFormLayout.FieldRole, self.valueLabel_53)

        self.valueLabel_54 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_54.setObjectName(u"valueLabel_54")
        self.valueLabel_54.setFont(font4)

        self.formLayout_2.setWidget(54, QFormLayout.FieldRole, self.valueLabel_54)

        self.valueLabel_55 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_55.setObjectName(u"valueLabel_55")
        self.valueLabel_55.setFont(font4)

        self.formLayout_2.setWidget(55, QFormLayout.FieldRole, self.valueLabel_55)

        self.valueLabel_56 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_56.setObjectName(u"valueLabel_56")
        self.valueLabel_56.setFont(font4)

        self.formLayout_2.setWidget(56, QFormLayout.FieldRole, self.valueLabel_56)

        self.valueLabel_57 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_57.setObjectName(u"valueLabel_57")
        self.valueLabel_57.setFont(font4)

        self.formLayout_2.setWidget(57, QFormLayout.FieldRole, self.valueLabel_57)

        self.valueLabel_58 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_58.setObjectName(u"valueLabel_58")
        self.valueLabel_58.setFont(font4)

        self.formLayout_2.setWidget(58, QFormLayout.FieldRole, self.valueLabel_58)

        self.valueLabel_59 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_59.setObjectName(u"valueLabel_59")
        self.valueLabel_59.setFont(font4)

        self.formLayout_2.setWidget(59, QFormLayout.FieldRole, self.valueLabel_59)

        self.valueLabel_60 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_60.setObjectName(u"valueLabel_60")
        self.valueLabel_60.setFont(font4)

        self.formLayout_2.setWidget(60, QFormLayout.FieldRole, self.valueLabel_60)

        self.addrLabel_61 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_61.setObjectName(u"addrLabel_61")
        self.addrLabel_61.setFont(font4)

        self.formLayout_2.setWidget(61, QFormLayout.LabelRole, self.addrLabel_61)

        self.addrLabel_62 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_62.setObjectName(u"addrLabel_62")
        self.addrLabel_62.setFont(font4)

        self.formLayout_2.setWidget(62, QFormLayout.LabelRole, self.addrLabel_62)

        self.addrLabel_63 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_63.setObjectName(u"addrLabel_63")
        self.addrLabel_63.setFont(font4)

        self.formLayout_2.setWidget(63, QFormLayout.LabelRole, self.addrLabel_63)

        self.addrLabel_64 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_64.setObjectName(u"addrLabel_64")
        self.addrLabel_64.setFont(font4)

        self.formLayout_2.setWidget(64, QFormLayout.LabelRole, self.addrLabel_64)

        self.addrLabel_65 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_65.setObjectName(u"addrLabel_65")
        self.addrLabel_65.setFont(font4)

        self.formLayout_2.setWidget(65, QFormLayout.LabelRole, self.addrLabel_65)

        self.addrLabel_66 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_66.setObjectName(u"addrLabel_66")
        self.addrLabel_66.setFont(font4)

        self.formLayout_2.setWidget(66, QFormLayout.LabelRole, self.addrLabel_66)

        self.addrLabel_67 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_67.setObjectName(u"addrLabel_67")
        self.addrLabel_67.setFont(font4)

        self.formLayout_2.setWidget(67, QFormLayout.LabelRole, self.addrLabel_67)

        self.addrLabel_68 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_68.setObjectName(u"addrLabel_68")
        self.addrLabel_68.setFont(font4)

        self.formLayout_2.setWidget(68, QFormLayout.LabelRole, self.addrLabel_68)

        self.addrLabel_69 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_69.setObjectName(u"addrLabel_69")
        self.addrLabel_69.setFont(font4)

        self.formLayout_2.setWidget(69, QFormLayout.LabelRole, self.addrLabel_69)

        self.addrLabel_70 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_70.setObjectName(u"addrLabel_70")
        self.addrLabel_70.setFont(font4)

        self.formLayout_2.setWidget(70, QFormLayout.LabelRole, self.addrLabel_70)

        self.valueLabel_61 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_61.setObjectName(u"valueLabel_61")
        self.valueLabel_61.setFont(font4)

        self.formLayout_2.setWidget(61, QFormLayout.FieldRole, self.valueLabel_61)

        self.valueLabel_62 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_62.setObjectName(u"valueLabel_62")
        self.valueLabel_62.setFont(font4)

        self.formLayout_2.setWidget(62, QFormLayout.FieldRole, self.valueLabel_62)

        self.valueLabel_63 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_63.setObjectName(u"valueLabel_63")
        self.valueLabel_63.setFont(font4)

        self.formLayout_2.setWidget(63, QFormLayout.FieldRole, self.valueLabel_63)

        self.valueLabel_64 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_64.setObjectName(u"valueLabel_64")
        self.valueLabel_64.setFont(font4)

        self.formLayout_2.setWidget(64, QFormLayout.FieldRole, self.valueLabel_64)

        self.valueLabel_65 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_65.setObjectName(u"valueLabel_65")
        self.valueLabel_65.setFont(font4)

        self.formLayout_2.setWidget(65, QFormLayout.FieldRole, self.valueLabel_65)

        self.valueLabel_66 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_66.setObjectName(u"valueLabel_66")
        self.valueLabel_66.setFont(font4)

        self.formLayout_2.setWidget(66, QFormLayout.FieldRole, self.valueLabel_66)

        self.valueLabel_67 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_67.setObjectName(u"valueLabel_67")
        self.valueLabel_67.setFont(font4)

        self.formLayout_2.setWidget(67, QFormLayout.FieldRole, self.valueLabel_67)

        self.valueLabel_68 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_68.setObjectName(u"valueLabel_68")
        self.valueLabel_68.setFont(font4)

        self.formLayout_2.setWidget(68, QFormLayout.FieldRole, self.valueLabel_68)

        self.valueLabel_69 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_69.setObjectName(u"valueLabel_69")
        self.valueLabel_69.setFont(font4)

        self.formLayout_2.setWidget(69, QFormLayout.FieldRole, self.valueLabel_69)

        self.valueLabel_70 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_70.setObjectName(u"valueLabel_70")
        self.valueLabel_70.setFont(font4)

        self.formLayout_2.setWidget(70, QFormLayout.FieldRole, self.valueLabel_70)

        self.addrLabel_71 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_71.setObjectName(u"addrLabel_71")
        self.addrLabel_71.setFont(font4)

        self.formLayout_2.setWidget(71, QFormLayout.LabelRole, self.addrLabel_71)

        self.addrLabel_72 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_72.setObjectName(u"addrLabel_72")
        self.addrLabel_72.setFont(font4)

        self.formLayout_2.setWidget(72, QFormLayout.LabelRole, self.addrLabel_72)

        self.addrLabel_73 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_73.setObjectName(u"addrLabel_73")
        self.addrLabel_73.setFont(font4)

        self.formLayout_2.setWidget(73, QFormLayout.LabelRole, self.addrLabel_73)

        self.addrLabel_74 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_74.setObjectName(u"addrLabel_74")
        self.addrLabel_74.setFont(font4)

        self.formLayout_2.setWidget(74, QFormLayout.LabelRole, self.addrLabel_74)

        self.addrLabel_75 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_75.setObjectName(u"addrLabel_75")
        self.addrLabel_75.setFont(font4)

        self.formLayout_2.setWidget(75, QFormLayout.LabelRole, self.addrLabel_75)

        self.addrLabel_76 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_76.setObjectName(u"addrLabel_76")
        self.addrLabel_76.setFont(font4)

        self.formLayout_2.setWidget(76, QFormLayout.LabelRole, self.addrLabel_76)

        self.addrLabel_77 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_77.setObjectName(u"addrLabel_77")
        self.addrLabel_77.setFont(font4)

        self.formLayout_2.setWidget(77, QFormLayout.LabelRole, self.addrLabel_77)

        self.addrLabel_78 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_78.setObjectName(u"addrLabel_78")
        self.addrLabel_78.setFont(font4)

        self.formLayout_2.setWidget(78, QFormLayout.LabelRole, self.addrLabel_78)

        self.addrLabel_79 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_79.setObjectName(u"addrLabel_79")
        self.addrLabel_79.setFont(font4)

        self.formLayout_2.setWidget(79, QFormLayout.LabelRole, self.addrLabel_79)

        self.addrLabel_80 = QLabel(self.scrollAreaWidgetContents_2)
        self.addrLabel_80.setObjectName(u"addrLabel_80")
        self.addrLabel_80.setFont(font4)

        self.formLayout_2.setWidget(80, QFormLayout.LabelRole, self.addrLabel_80)

        self.valueLabel_71 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_71.setObjectName(u"valueLabel_71")
        self.valueLabel_71.setFont(font4)

        self.formLayout_2.setWidget(71, QFormLayout.FieldRole, self.valueLabel_71)

        self.valueLabel_72 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_72.setObjectName(u"valueLabel_72")
        self.valueLabel_72.setFont(font4)

        self.formLayout_2.setWidget(72, QFormLayout.FieldRole, self.valueLabel_72)

        self.valueLabel_73 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_73.setObjectName(u"valueLabel_73")
        self.valueLabel_73.setFont(font4)

        self.formLayout_2.setWidget(73, QFormLayout.FieldRole, self.valueLabel_73)

        self.valueLabel_74 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_74.setObjectName(u"valueLabel_74")
        self.valueLabel_74.setFont(font4)

        self.formLayout_2.setWidget(74, QFormLayout.FieldRole, self.valueLabel_74)

        self.valueLabel_75 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_75.setObjectName(u"valueLabel_75")
        self.valueLabel_75.setFont(font4)

        self.formLayout_2.setWidget(75, QFormLayout.FieldRole, self.valueLabel_75)

        self.valueLabel_76 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_76.setObjectName(u"valueLabel_76")
        self.valueLabel_76.setFont(font4)

        self.formLayout_2.setWidget(76, QFormLayout.FieldRole, self.valueLabel_76)

        self.valueLabel_77 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_77.setObjectName(u"valueLabel_77")
        self.valueLabel_77.setFont(font4)

        self.formLayout_2.setWidget(77, QFormLayout.FieldRole, self.valueLabel_77)

        self.valueLabel_78 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_78.setObjectName(u"valueLabel_78")
        self.valueLabel_78.setFont(font4)

        self.formLayout_2.setWidget(78, QFormLayout.FieldRole, self.valueLabel_78)

        self.valueLabel_79 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_79.setObjectName(u"valueLabel_79")
        self.valueLabel_79.setFont(font4)

        self.formLayout_2.setWidget(79, QFormLayout.FieldRole, self.valueLabel_79)

        self.valueLabel_80 = QLabel(self.scrollAreaWidgetContents_2)
        self.valueLabel_80.setObjectName(u"valueLabel_80")
        self.valueLabel_80.setFont(font4)

        self.formLayout_2.setWidget(80, QFormLayout.FieldRole, self.valueLabel_80)

        self.memoriaArea.setWidget(self.scrollAreaWidgetContents_2)
        unicicloWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(unicicloWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 863, 22))
        unicicloWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(unicicloWindow)
        self.statusbar.setObjectName(u"statusbar")
        unicicloWindow.setStatusBar(self.statusbar)

        self.retranslateUi(unicicloWindow)

        QMetaObject.connectSlotsByName(unicicloWindow)
    # setupUi

    def retranslateUi(self, unicicloWindow):
        unicicloWindow.setWindowTitle(QCoreApplication.translate("unicicloWindow", u"unicicloWindow", None))
        self.label.setText(QCoreApplication.translate("unicicloWindow", u"Numero de ciclo", None))
        self.pcLabel.setText(QCoreApplication.translate("unicicloWindow", u"pcLabel", None))
        self.pcNumberLabel.setText(QCoreApplication.translate("unicicloWindow", u"NUM PC", None))
        self.registroMainLabel.setText(QCoreApplication.translate("unicicloWindow", u"Registros", None))
        self.rxMainLabel_2.setText(QCoreApplication.translate("unicicloWindow", u"RX", None))
        self.valueRegistrosLabel_2.setText(QCoreApplication.translate("unicicloWindow", u"Value", None))
        self.rxLabel.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_2.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_2.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_3.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_3.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_4.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_4.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_5.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_5.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_10.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_9.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_8.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_7.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_6.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_6.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_7.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_8.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_9.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_10.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_11.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_11.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_12.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_12.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_22.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_21.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_20.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_19.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_18.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_17.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_16.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_15.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_14.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_13.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_13.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_14.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_15.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_16.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_17.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_18.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_19.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_20.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_21.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_22.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_23.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_24.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_25.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_26.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_27.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_28.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_29.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_30.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_31.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.rxLabel_32.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_23.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_24.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_25.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_26.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_27.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_28.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_29.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_30.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_31.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueRegLabel_32.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.memoriaMainLabel.setText(QCoreApplication.translate("unicicloWindow", u"Memoria", None))
        self.rxMainLabel_3.setText(QCoreApplication.translate("unicicloWindow", u"addr", None))
        self.valueRegistrosLabel_3.setText(QCoreApplication.translate("unicicloWindow", u"Value", None))
        self.addrLabel.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_2.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_2.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_3.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_3.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_4.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_4.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_5.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_5.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_6.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_6.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_7.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_7.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_8.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_8.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_9.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_9.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_10.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_10.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_16.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_11.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_18.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_12.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_14.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_13.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_12.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_14.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_11.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_15.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_15.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_16.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_17.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_17.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_13.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_18.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_19.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_19.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_20.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_20.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_21.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_21.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_22.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_23.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_31.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_28.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_26.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_24.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_27.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_30.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_25.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_29.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_22.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_23.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_24.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_25.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_26.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_27.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_28.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_29.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_30.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_31.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_32.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_33.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_34.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_35.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_36.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_37.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_38.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_39.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_40.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_32.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_33.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_34.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_35.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_36.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_37.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_38.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_39.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_40.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_41.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_42.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_43.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_44.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_45.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_46.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_47.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_48.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_49.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_50.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_41.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_42.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_43.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_44.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_45.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_46.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_47.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_48.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_49.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_50.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_51.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_52.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_53.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_54.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_55.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_56.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_57.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_58.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_59.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_60.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_51.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_52.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_53.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_54.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_55.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_56.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_57.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_58.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_59.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_60.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_61.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_62.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_63.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_64.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_65.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_66.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_67.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_68.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_69.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_70.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_61.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_62.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_63.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_64.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_65.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_66.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_67.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_68.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_69.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_70.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_71.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_72.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_73.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_74.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_75.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_76.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_77.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_78.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_79.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.addrLabel_80.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_71.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_72.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_73.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_74.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_75.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_76.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_77.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_78.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_79.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
        self.valueLabel_80.setText(QCoreApplication.translate("unicicloWindow", u"TextLabel", None))
    # retranslateUi

