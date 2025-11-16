import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QSlider, QPushButton,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Desafío Final de Layouts")
        self.setMinimumSize(QSize(500, 400))

        # --- WIDGETS CREADOS ---

        # Comandos para el QGridLayout (Componente 1)
        lblHP = QLabel("HP:")
        lblATK = QLabel("ATK:")
        lblValorHP = QLabel("8000")
        lblValorATK = QLabel("4500")

        # Widget para el medio (Componente 2)
        sldVelocidad = QSlider(Qt.Orientation.Horizontal)

        # Comandos para el QHBoxLayout (Componente 3)
        btnAceptar = QPushButton("Aceptar")
        btnCancelar = QPushButton("Cancelar")

        # --- SOLUCIÓN DEL LAYOUT ---

        # 1. Crea el QWidget central y el QVBoxLayout principal.
        widgetPrincipal = QWidget()
        self.setCentralWidget(widgetPrincipal)

        layoutPrincipal = QVBoxLayout()
        widgetPrincipal.setLayout(layoutPrincipal)  # ¡El layout se aplica al widget!

        # 2. Crea el QGridLayout (Componente 1: Estadísticas 2x2)
        layoutEstadisticas = QGridLayout()

        # Fila 0: HP y su valor
        layoutEstadisticas.addWidget(lblHP, 0, 0)
        layoutEstadisticas.addWidget(lblValorHP, 0, 1)

        # Fila 1: ATK y su valor
        layoutEstadisticas.addWidget(lblATK, 1, 0)
        layoutEstadisticas.addWidget(lblValorATK, 1, 1)

        # 3. Crea el QHBoxLayout (Componente 3: Botones)
        layoutBotones = QHBoxLayout()
        layoutBotones.addWidget(btnAceptar)
        layoutBotones.addWidget(btnCancelar)

        # 4. Añade los 3 componentes al QVBoxLayout principal en orden:

        # 1º: El QGridLayout (Componente 1)
        layoutPrincipal.addLayout(layoutEstadisticas)

        # 2º: El QSlider (Componente 2) - Añadido directamente
        layoutPrincipal.addWidget(sldVelocidad)

        # 3º: El QHBoxLayout (Componente 3)
        layoutPrincipal.addLayout(layoutBotones)

        self.show()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    sys.exit(aplicacion.exec())