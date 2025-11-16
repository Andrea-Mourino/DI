import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QCheckBox, QTextEdit, QPushButton,
                             QWidget, QVBoxLayout, QHBoxLayout)


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejercicio de Layouts")
        self.setMinimumSize(QSize(400, 300))

        # --- WIDGETS CREADOS ---
        self.editorTexto = QTextEdit()
        btnA = QPushButton("A")
        btnB = QPushButton("B")
        btnC = QPushButton("C")
        chkMision = QCheckBox("Misión Completa")

        # --- TU CÓDIGO VA AQUÍ ---
        # 1. Crea el QWidget central.
        # 2. Crea el QVBoxLayout principal y aplícalo al widget central.
        # 3. Crea el QHBoxLayout para los botones.
        # 4. Añade los widgets y layouts al layout principal en el orden correcto.

        widgetCentral = QWidget()
        self.setCentralWidget(widgetCentral)

        layoutPrincipal = QVBoxLayout()
        widgetCentral.setLayout(layoutPrincipal)


        layoutBotonesPrincipales = QHBoxLayout()
        layoutBotonesPrincipales.addWidget(btnA)
        layoutBotonesPrincipales.addWidget(btnB)
        layoutBotonesPrincipales.addWidget(btnC)


        layoutOpcoesGrupo = QVBoxLayout()
        layoutPrincipal.addWidget(self.editorTexto)
        layoutPrincipal.addLayout(layoutBotonesPrincipales)
        layoutOpcoesGrupo.addWidget(chkMision)



        self.show()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    sys.exit(aplicacion.exec())