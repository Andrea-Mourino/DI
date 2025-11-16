import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QCheckBox, QTextEdit, QPushButton, QComboBox, QSlider,
                             QGroupBox, QDial)


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Configuración de Personaje - Simulación")
        self.setMinimumSize(QSize(500, 500))

        # --- INSTANCIACIÓN DE WIDGETS (CÓDIGO COMPLETO) ---

        # 1. Área Principal (QTextEdit)
        self.txtBiografia = QTextEdit()

        # 2. Botones de Acción (QPushButton)
        self.btnGuardar = QPushButton("Guardar")
        self.btnCargar = QPushButton("Cargar")
        self.btnReiniciar = QPushButton("Reiniciar")

        # 3. Controles Deslizantes (QLabel y QSlider)
        self.lblFuerza = QLabel("Fuerza:")
        self.sldFuerza = QSlider(Qt.Orientation.Horizontal)  # ¡Horizontal es clave!
        self.lblDefensa = QLabel("Defensa:")
        self.sldDefensa = QSlider(Qt.Orientation.Horizontal)

        # 4. Grupo de Opciones (QGroupBox y QCheckBox)
        self.grpClaseCombate = QGroupBox("Clase de Combate")  # El título va en el constructor del QGroupBox
        self.chkFisico = QCheckBox("Físico")
        self.chkCuantico = QCheckBox("Cuántico")
        self.chkImaginario = QCheckBox("Imaginario")

        # 5. Selector Principal (QComboBox)
        self.cmbVia = QComboBox()
        # (Nota: En un programa real, aquí añadirías opciones: self.cmbVia.addItems(["Cacería", "Destrucción", "Preservación"]))

        # --- FIN DE INSTANCIACIÓN ---

        self.show()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    sys.exit(aplicacion.exec())