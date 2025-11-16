import sys

from PyQt6.QtWidgets import QWidget, QGridLayout, QLineEdit, QLabel, QComboBox, QPushButton, QApplication, QVBoxLayout, \
    QTextEdit


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.show()

    def inicializarUI(self):

        self.maya1 =QGridLayout()


        self.labelName = QLabel("Nombre")
        self.inputName = QLineEdit()

        self.labelCarpeta = QLabel("Carpeta")
        self.carpetasDesplegable = QComboBox()
        self.carpetasDesplegable.addItems(["carpeta1", "carpeta2", "carpeta3"])

        self.labelDescripcion = QLabel("Descripción")
        self.inputDescripcion = QLineEdit()


        self.labelRuta = QLabel("Ruta")
        self.inputRuta = QLineEdit()
        self.buttonRuta = QPushButton()

        self.buttonViewImage = QPushButton("Ver Foto")
        self.buttonClear = QPushButton("Borrar")
        self.buttonSave = QPushButton("Guardar")




        self.maya1.addWidget(self.labelName,0,0)
        self.maya1.addWidget(self.inputName,0,1,1,4)

        self.maya1.addWidget(self.labelCarpeta,1,0)
        self.maya1.addWidget(self.carpetasDesplegable,1,1,1,4)

        self.maya1.addWidget(self.labelDescripcion,2,0)
        self.maya1.addWidget(self.inputDescripcion,2,1,1,4)

        self.maya1.addWidget(self.labelRuta,3,0)
        self.maya1.addWidget(self.inputRuta,3,1,1,4)
        self.maya1.addWidget(self.buttonRuta,3,5)

        self.maya1.addWidget(self.buttonViewImage,4,0,1,2)
        self.maya1.addWidget(self.buttonClear,4,2,1,2)
        self.maya1.addWidget(self.buttonSave,4,4,1,2)

        boxVertical=QVBoxLayout()

        self.text = QTextEdit()

        boxVertical.addLayout(self.maya1)
        boxVertical.addWidget(self.text)


        self.setLayout(boxVertical)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Menu()
    sys.exit(app.exec())