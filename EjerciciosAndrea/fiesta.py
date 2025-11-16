import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QCheckBox, QTextEdit, QPushButton,
    QComboBox, QSlider, QGroupBox, QDial, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog
)


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exame 17-12-2024")
        self.setMinimumSize(QSize(700, 500))

        # ----------------------
        # Widgets principales
        # ----------------------
        self.tedCadroTexto = QTextEdit()

        self.btnAbrirFich = QPushButton("Abrir ficheiro")
        btnReproducir = QPushButton("Reproducir ficheiro")
        btnGardar = QPushButton("Gardar")
        btnEliminar = QPushButton("Eliminar")
        dilVolume = QDial()
        chkAnimado = QCheckBox("Animado")

        btnSaltar = QPushButton("Saltar")
        cmbSaltar = QComboBox()
        cmbSaltar.addItems(["5s", "10s", "30s"])  # ejemplo de opciones

        # ----------------------
        # Opcions Reproduccion
        # ----------------------
        opcionsReproduccion = QGroupBox("Opcións de reprodución")
        chkFiltrar = QCheckBox("Filtrar antes de reproducir")
        chkEXML = QCheckBox("É XML")
        chkRepNPL = QCheckBox("Reproducción NPL")

        lblVolume = QLabel("Volume:")
        lblFormato = QLabel("Formato:")
        lblSaidaAudio = QLabel("SaidaAudio:")

        sldVolume = QSlider(Qt.Orientation.Horizontal)
        cmbFormato = QComboBox()
        cmbFormato.addItems(["MP3", "WAV", "FLAC"])
        cmbSaidaAudio = QComboBox()
        cmbSaidaAudio.addItems(["Altavoces", "Auriculares", "HDMI"])

        # ----------------------
        # Conexión del botón "Abrir ficheiro"
        # ----------------------
        self.btnAbrirFich.clicked.connect(self.abrir_fichero)

        # ----------------------
        # Layouts
        # ----------------------
        layoutPrincipal = QVBoxLayout()

        # Área de texto arriba
        layoutPrincipal.addWidget(self.tedCadroTexto)

        # Layout horizontal para botones principales
        layoutBotons = QHBoxLayout()
        layoutBotons.addWidget(self.btnAbrirFich)
        layoutBotons.addWidget(btnReproducir)
        layoutBotons.addWidget(btnGardar)
        layoutBotons.addWidget(btnEliminar)
        layoutBotons.addWidget(chkAnimado)
        layoutPrincipal.addLayout(layoutBotons)

        # Layout horizontal para saltar
        layoutSaltar = QHBoxLayout()
        layoutSaltar.addWidget(btnSaltar)
        layoutSaltar.addWidget(cmbSaltar)
        layoutPrincipal.addLayout(layoutSaltar)

        # Layout opciones de reproducción
        layoutOpcions = QVBoxLayout()
        layoutOpcions.addWidget(chkFiltrar)
        layoutOpcions.addWidget(chkEXML)
        layoutOpcions.addWidget(chkRepNPL)
        layoutOpcions.addWidget(lblVolume)
        layoutOpcions.addWidget(sldVolume)
        layoutOpcions.addWidget(lblFormato)
        layoutOpcions.addWidget(cmbFormato)
        layoutOpcions.addWidget(lblSaidaAudio)
        layoutOpcions.addWidget(cmbSaidaAudio)
        layoutOpcions.addWidget(dilVolume)
        opcionsReproduccion.setLayout(layoutOpcions)

        layoutPrincipal.addWidget(opcionsReproduccion)

        # ----------------------
        # Contenedor central
        # ----------------------
        contenedor = QWidget()
        contenedor.setLayout(layoutPrincipal)
        self.setCentralWidget(contenedor)

    # ----------------------
    # Método para abrir archivo
    # ----------------------
    def abrir_fichero(self):
        ruta, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar archivo",
            "",
            "Todos los archivos (*);;Imágenes (*.png *.jpg *.jpeg);;Videos (*.mp4 *.avi *.mov)"
        )
        if ruta:
            # Mostrar la ruta en el QTextEdit
            self.tedCadroTexto.setText(ruta)


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    fiestra.show()
    sys.exit(aplicacion.exec())
