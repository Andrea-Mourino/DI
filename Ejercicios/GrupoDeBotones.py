import sys

from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QGroupBox


class ventanaBotones(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.show()

    def inicializarUI(self):
        self.bMortadelo = QPushButton("Mortadelo")
        self.bFilemon = QPushButton("Filemon")
        self.bCarpanta = QPushButton("Carpanta")
        self.bRompetechos = QPushButton("Rompetechos")
        self.bPepeGotera = QPushButton("Pepe Gotera")
        self.bOtilio = QPushButton("Otilio")

        self.cajaHorizontal1 = QHBoxLayout()
        self.cajaHorizontal1.addWidget(self.bMortadelo)
        self.cajaHorizontal1.addWidget(self.bFilemon)
        self.cajaHorizontal1.addWidget(self.bCarpanta)
        self.cajaHorizontal1.addWidget(self.bRompetechos)
        self.cajaHorizontal1.addWidget(self.bPepeGotera)
        self.cajaHorizontal1.addWidget(self.bOtilio)


        self.group = QGroupBox("Push Buttons")
        self.group.setLayout(self.cajaHorizontal1)

        self.tMortadelo = QPushButton("Mortadelo")
        self.tFilemon = QPushButton("Filemon")
        self.tCarpanta = QPushButton("Carpanta")
        self.tRompetechos = QPushButton("Rompetechos")
        self.tPepeGotera = QPushButton("Pepe Gotera")
        self.tOtilio = QPushButton("Otilio")

        self.tMortadelo.setCheckable(True)
        self.tMortadelo.setChecked(False)
        self.tFilemon.setCheckable(True)
        self.tFilemon.setChecked(False)
        self.tCarpanta.setCheckable(True)
        self.tCarpanta.setChecked(False)
        self.tRompetechos.setCheckable(True)
        self.tRompetechos.setChecked(False)
        self.tPepeGotera.setCheckable(True)
        self.tPepeGotera.setChecked(False)
        self.tOtilio.setCheckable(True)
        self.tOtilio.setChecked(False)

        self.cajaHorizontal2 = QHBoxLayout()
        self.cajaHorizontal2.addWidget(self.tMortadelo)
        self.cajaHorizontal2.addWidget(self.tFilemon)
        self.cajaHorizontal2.addWidget(self.tCarpanta)
        self.cajaHorizontal2.addWidget(self.tRompetechos)
        self.cajaHorizontal2.addWidget(self.tPepeGotera)
        self.cajaHorizontal2.addWidget(self.tOtilio)

        self.group2 = QGroupBox("Toggle Buttons")
        self.group2.setLayout(self.cajaHorizontal2)

        self.cajaVertical = QVBoxLayout()
        self.cajaVertical.addWidget(self.group)
        self.cajaVertical.addWidget(self.group2)

        self.setLayout(self.cajaVertical)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = ventanaBotones()
    sys.exit(app.exec())