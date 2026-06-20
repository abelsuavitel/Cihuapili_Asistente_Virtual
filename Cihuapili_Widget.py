import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.Aparecer()

    def Aparecer(self):
        #Configuracion de la ventana
        self.setGeometry(1143, 600, 200, 175)
        self.setWindowTitle("Cihuapilli")
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |  
            Qt.WindowType.WindowStaysOnTopHint   
        )

        #Configuracion de la imagen
        CihuapiliCara = "Teto.png"
        pixmap = QPixmap(CihuapiliCara)
        self.lbl = QLabel(self)
        self.lbl.setPixmap(pixmap)
        self.lbl.setStyleSheet("background: transparent;")
        self.lbl.setFixedSize(pixmap.width(), pixmap.height())
        self.setFixedSize(pixmap.width(), pixmap.height())

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Ventana = Widget()
    sys.exit(app.exec())