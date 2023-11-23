import sys

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formhsKdUn.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PyQt6 import QtWidgets
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


from View.seleccionProc_ui import Ui_seleccionProceWindow

app = QtWidgets.QApplication(sys.argv)


class seleccionProceWindow(QMainWindow, Ui_seleccionProceWindow):
    def __int__(self):
        super().__init__()
        
        

window = seleccionProceWindow()
window.setupUi(window)
window.show()
sys.exit(app.exec())
