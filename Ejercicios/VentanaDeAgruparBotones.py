import sys

from PyQt6.QtWidgets import (QApplication, QWidget, QRadioButton,
                             QVBoxLayout, QHBoxLayout, QTextEdit, QLabel,
                             QButtonGroup)

class trabajandoConGrupos(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.show()

    def inicializarUI(self):
        self.boton1 = QRadioButton("Libre")
        self.boton2 = QRadioButton("Agrupado1")
        self.boton3 = QRadioButton("Agrupado2")
        self.boton4 = QRadioButton("Agrupado3")

        # QButtonGroup es solo un contenedor lógico (no es un QLayout).
        # Se usa para gestionar exclusividad/señales, no para añadir al layout.
        self.grupo = QButtonGroup()
        self.grupo.addButton(self.boton2)
        self.grupo.addButton(self.boton3)
        self.grupo.addButton(self.boton4)

        self.cajaHorizontal = QHBoxLayout()

        # Crear un QLayout real para los botones del grupo y añadir los widgets.
        self.grupoLayout = QVBoxLayout()  # layout físico para los radio buttons agrupados
        self.grupoLayout.addWidget(self.boton2)
        self.grupoLayout.addWidget(self.boton3)
        self.grupoLayout.addWidget(self.boton4)

        # Añadir el layout del grupo al layout horizontal (corrección:
        # antes intentabas añadir QButtonGroup con addLayout, eso daba TypeError).
        self.cajaHorizontal.addLayout(self.grupoLayout)

        # Añadir el botón independiente como widget (no como layout).
        self.cajaHorizontal.addWidget(self.boton1)

        self.setLayout(self.cajaHorizontal)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = trabajandoConGrupos()
    sys.exit(app.exec())


