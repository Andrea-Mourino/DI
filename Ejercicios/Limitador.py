import sys

from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QLineEdit, QPushButton, QCheckBox, QRadioButton,
                             QVBoxLayout, QComboBox, QSpinBox, QHBoxLayout, QTextEdit)

class Limitador(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

        self.show()

    def inicializarUI(self):

        self.cajaVerticalRadioButton()

        self.cajaVerticalCheckButton()

        self.cajaVerticalImputs()

        self.cajaHorizontal = QHBoxLayout()

        self.cajaHorizontal.addLayout(self.verticalCaja1)
        self.cajaHorizontal.addLayout(self.verticalCaja2)
        self.cajaHorizontal.addLayout(self.cajaImputs)


        self.texto = QTextEdit()
        self.texto.setPlaceholderText("Original")
        self.texto.setReadOnly(True)
        self.texto.setFixedHeight(35)
        self.cajaV = QVBoxLayout()

        self.cajaV.addWidget(self.texto)
        self.cajaV.addLayout(self.cajaHorizontal)


        self.setLayout(self.cajaV)



    def cajaVerticalImputs(self):
        self.inputText = QLineEdit()
        self.desplegable = QComboBox()
        self.inputNumber = QSpinBox()

        self.desplegable.addItems(["Item 1", "Item 2", "Item 3"])

        self.cajaImputs = QVBoxLayout()

        self.cajaImputs.addWidget(self.inputText)
        self.cajaImputs.addWidget(self.desplegable)
        self.cajaImputs.addWidget(self.inputNumber)


    def cajaVerticalCheckButton(self):
        self.cuadroCheck1 = QCheckBox("Opcion 4")
        self.cuadroCheck2 = QCheckBox("Opcion 5")
        self.cuadroCheck3 = QCheckBox("Opcion 6")

        self.verticalCaja2 = QVBoxLayout()

        self.verticalCaja2.addWidget(self.cuadroCheck1)
        self.verticalCaja2.addWidget(self.cuadroCheck2)
        self.verticalCaja2.addWidget(self.cuadroCheck3)



    def cajaVerticalRadioButton(self):
        self.boton1 = QRadioButton("Opcion 1")
        self.boton2 = QRadioButton("Opcion 2")
        self.boton3 = QRadioButton("Opcion 3")

        self.verticalCaja1 = QVBoxLayout()
        self.verticalCaja1.addWidget(self.boton1)
        self.verticalCaja1.addWidget(self.boton2)
        self.verticalCaja1.addWidget(self.boton3)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Limitador()
    sys.exit(app.exec())