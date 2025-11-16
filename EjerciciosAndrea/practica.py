import sys

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import (
    QApplication, QWidget, QGroupBox, QGridLayout, QTextEdit, QLineEdit,
    QVBoxLayout, QTabWidget, QCheckBox, QSlider, QListView, QPushButton,
    QHBoxLayout, QLabel
)


class VentanaSimple(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.show()

    def inicializarUI(self):
        self.setMinimumSize(QSize(600, 400))
        self.setWindowTitle("Ventana MIA")

        # Panel superior izquierda (lista + botones)
        self.pestañaItemsBotones = QGroupBox("Panel")

        # Área de texto grande (abajo derecha)
        self.espacioTexto = QTextEdit()

        # Crear las partes
        self.crearItems()
        self.crearBotones()
        self.crearPestañas()
        self.crearTextoEnLinea()

        # Layout horizontal para el panel (LISTA + BOTONES)
        self.PanelHorizontalIzquierdaArriba = QHBoxLayout()
        self.PanelHorizontalIzquierdaArriba.addWidget(self.listaView)
        self.PanelHorizontalIzquierdaArriba.addLayout(self.cajaBotones)

        self.pestañaItemsBotones.setLayout(self.PanelHorizontalIzquierdaArriba)

        # ---------- GRID PRINCIPAL ----------
        self.grid = QGridLayout()

        self.grid.addWidget(self.pestañaItemsBotones, 0, 0)
        self.grid.addLayout(self.horizontal, 1, 0)
        self.grid.addWidget(self.ventanas, 0, 1)
        self.grid.addWidget(self.espacioTexto, 1, 1)

        self.setLayout(self.grid)

    # ---------------------------------------
    # MÉTODOS DE CREACIÓN DE COMPONENTES
    # ---------------------------------------

    def crearItems(self):
        self.listaView = QListView()
        self.listaModelo = QStandardItemModel()

        # Crear items
        for texto in ("Item 1", "Item 2", "Item 3"):
            self.listaModelo.appendRow(QStandardItem(texto))

        self.listaView.setModel(self.listaModelo)

    def crearBotones(self):
        self.cajaBotones = QVBoxLayout()
        self.btn1 = QPushButton("Boton1")
        self.btn2 = QPushButton("Boton2")

        self.cajaBotones.addWidget(self.btn1)
        self.cajaBotones.addWidget(self.btn2)

    def crearPestañas(self):
        self.ventanas = QTabWidget()

        # ---- TAB 1 ----
        self.tab1 = QWidget()
        layout1 = QVBoxLayout()

        self.casilla1 = QCheckBox("CheckedCheckBox")
        self.casilla1.setChecked(True)

        self.slider1 = QSlider(Qt.Orientation.Horizontal)

        layout1.addWidget(self.casilla1)
        layout1.addWidget(self.slider1)
        self.tab1.setLayout(layout1)

        # ---- TAB 2 ----
        self.tab2 = QWidget()
        layout2 = QVBoxLayout()

        self.labelHola = QLabel("Hola")
        layout2.addWidget(self.labelHola)

        self.tab2.setLayout(layout2)

        self.ventanas.addTab(self.tab1, "SelecTab")
        self.ventanas.addTab(self.tab2, "OtherTab")

    def crearTextoEnLinea(self):
        self.texto = QLineEdit("Text Field")

        self.horizontal = QHBoxLayout()
        self.horizontal.addWidget(self.texto)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaSimple()
    sys.exit(app.exec())
