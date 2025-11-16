import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QTextEdit, QLineEdit,
                             QWidget, QVBoxLayout, QGridLayout, QHBoxLayout)  # <-- QLineEdit y QGridLayout añadidos


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejercicio de QGridLayout")
        self.setMinimumSize(QSize(400, 150))

        # --- WIDGETS CREADOS ---
        lblUsuario = QLabel("Usuario:")
        lblClave = QLabel("Clave:")

        inputUsuario = QTextEdit()  # Usaremos QTextEdit por ahora, aunque es un poco grande
        inputClave = QLineEdit()  # Este es el campo de una sola línea (ideal para la clave)

        # --- TU CÓDIGO VA AQUÍ ---
        # 1. Crea el QWidget central.
        # 2. Crea el QVBoxLayout principal y aplícalo.
        # 3. Crea el QGridLayout.
        # 4. Añade los 4 widgets al QGridLayout usando las coordenadas (fila, columna).
        # 5. Añade el QGridLayout al QVBoxLayout principal.

        widgetPrincipal = QWidget()
        self.setCentralWidget(widgetPrincipal)

        layoutPrincipal = QVBoxLayout()
        widgetPrincipal.setLayout(layoutPrincipal)

        layoutRejilla = QGridLayout()
        #Fila 1
        layoutRejilla.addWidget(lblUsuario,0,0)
        layoutRejilla.addWidget(lblClave,1, 0)

        layoutRejilla.addWidget(inputUsuario, 0, 1)
        layoutRejilla.addWidget(inputClave, 1, 1)

        layoutPrincipal.addLayout(layoutRejilla)
        layoutPrincipal.addStretch(1)

        self.show()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    sys.exit(aplicacion.exec())