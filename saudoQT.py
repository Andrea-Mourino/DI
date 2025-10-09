import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout)

class NosaPrimeiraFiestra (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A miña primeira fiestra con QT")
        """ self.setFixedSize( 400, 300 ) // para ajustar sin poder modificar la ventana"""
        self.setMinimumSize( 500, 300 )


        self.txtSaudo = QLineEdit()
        self.lblEtiqueta = QLabel("Ola a todos")
        fonte = self.lblEtiqueta.font()
        fonte.setPointSize(30)
        self.lblEtiqueta.sentFonte(fonte)
        self.lblEtiqueta.setAlignment(Qt.AligmentFlag.AlignHCenter| Qt.AligmentFlag.AlignVCenter)




        self.show()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = NosaPrimeiraFiestra()
    aplicacion.exec()

