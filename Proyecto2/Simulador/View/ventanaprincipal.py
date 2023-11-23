import sys

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

from seleccionProc_ui import Ui_seleccionProceWindow

app = QApplication(sys.argv)

class ventanaPrincipal(QMainWindow, Ui_seleccionProceWindow):
    def __int__(self):
        super().__init__()
        self.setupUi(self)
        #self.show()


window = ventanaPrincipal()
window.show()
sys.exit(app.exec())
