# PyQt6 – UI estilo "Mover hojas visibles/ocultas"
# Organizado por clases

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QListWidget, QPushButton,
    QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QMessageBox
)
from PyQt6.QtCore import Qt


# ------------------------------
# Panel principal con las listas
# ------------------------------
class SheetsPanel(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # --- Grupo: Hojas visibles ---
        group_visible = QGroupBox("Hojas visibles")
        visible_layout = QVBoxLayout()
        group_visible.setLayout(visible_layout)

        self.list_visible = QListWidget()
        self.list_visible.addItems(["Hoja4", "Hoja5", "Hoja6"])
        visible_layout.addWidget(self.list_visible)

        # --- Centro: botones mover ---
        center_layout = QVBoxLayout()

        self.btn_ocultar = QPushButton("Ocultar >>")
        self.btn_mostrar = QPushButton("<< Mostrar")
        center_layout.addStretch()
        center_layout.addWidget(self.btn_ocultar)
        center_layout.addWidget(self.btn_mostrar)
        center_layout.addStretch()

        # --- Grupo: Hojas ocultas ---
        group_hidden = QGroupBox("Hojas ocultas")
        hidden_layout = QVBoxLayout()
        group_hidden.setLayout(hidden_layout)

        self.list_hidden = QListWidget()
        self.list_hidden.addItems(["Hoja1", "Hoja2", "Hoja3"])
        hidden_layout.addWidget(self.list_hidden)

        # Agregar a la fila principal
        main_layout.addWidget(group_visible)
        main_layout.addLayout(center_layout)
        main_layout.addWidget(group_hidden)

        # Conexiones
        self.btn_ocultar.clicked.connect(self.move_visible_to_hidden)
        self.btn_mostrar.clicked.connect(self.move_hidden_to_visible)

    # --- Lógica mover listas ---
    def move_visible_to_hidden(self):
        item = self.list_visible.takeItem(self.list_visible.currentRow())
        if item:
            self.list_hidden.addItem(item.text())

    def move_hidden_to_visible(self):
        item = self.list_hidden.takeItem(self.list_hidden.currentRow())
        if item:
            self.list_visible.addItem(item.text())


# ------------------------------
# Ventana principal
# ------------------------------
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EXCELeINFO - Hojas")

        container = QWidget()
        layout = QVBoxLayout()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Panel principal
        self.sheets_panel = SheetsPanel()
        layout.addWidget(self.sheets_panel)

        # Botón cerrar
        btn_close = QPushButton("Cerrar")
        btn_close.clicked.connect(self.close)
        layout.addWidget(btn_close, alignment=Qt.AlignmentFlag.AlignRight)


# ------------------------------
# Lanzar aplicación
# ------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
