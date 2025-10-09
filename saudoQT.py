import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout)

class NosaPrimeiraFiestra (QMainWindow):
    def __init__(self):
        super().__init__()
        self.show()


if __name__="__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = NosaPrimeiraFiestra()
    aplicacion.exec()

