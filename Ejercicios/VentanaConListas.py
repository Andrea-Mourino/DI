import sys

from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import (QApplication, QWidget, QRadioButton,
                             QVBoxLayout, QHBoxLayout, QTextEdit, QLabel,
                             QButtonGroup, QPushButton, QListView)

class VentanaConListas(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.show()

    def inicializarUI(self):

        self.labelParaAñadirALista()
        self.lista()


        self.cajaVertical = QVBoxLayout()

        self.cajaVertical.addLayout(self.cajaHorizontal)
        self.cajaVertical.addWidget(self.lista1)

        self.setLayout(self.cajaVertical)


    def lista(self):
        self.model = QStandardItemModel()
        self.lista1 = QListView()



    def anadirElemento(self):
        text = self.label.toPlainText().strip()
        if not text:
            return
        self.itemPrueba = QStandardItem(text)
        self.model.appendRow(self.itemPrueba)
        self.lista1.setModel(self.model)

    def borrarUltimoElemento(self):
        if not hasattr(self, "model") or self.model is None:
            return
        count = self.model.rowCount()
        if count > 0:
            self.model.removeRow(count - 1)

    def labelParaAñadirALista(self):
        self.label = QTextEdit()
        self.botonAñadir = QPushButton("añadir")
        self.botonBorrar = QPushButton("borrar")
        self.cajaHorizontal = QHBoxLayout()
        self.cajaHorizontal.addWidget(self.label)
        self.cajaHorizontal.addWidget(self.botonAñadir)
        self.cajaHorizontal.addWidget(self.botonBorrar)

        self.botonBorrar.clicked.connect(self.borrarUltimoElemento)
        self.botonAñadir.clicked.connect(self.anadirElemento)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaConListas()
    sys.exit(app.exec())

    #self.itemPrueba = QStandardItem("Elemento de prueba")
    #self.model.appendRow(self.itemPrueba)
    #self.lista1.setModel(self.model)