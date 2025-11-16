import sys

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QApplication, QWidget, QGroupBox, QGridLayout, QTextEdit, QComboBox, QLineEdit, QVBoxLayout, \
    QTabWidget, QCheckBox, QSlider, QListView, QRadioButton, QPushButton, QHBoxLayout


class VentanaCopia(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.show()


    def inicializarUI(self):

        self.setMinimumSize(QSize(600, 450)) #tamaño ventana

        self.setWindowTitle("Mi Ventana") #titulo ventana

        self.grupoPanel = QGroupBox("Panel")

        self.espacioTexto = QTextEdit() #espacio de texto grande



#-----------CLASES------------
        self.primerPanelButtons()

        self.primerPanelList()

        self.paneles()

        self.pestañas()
# -----------------------------



# -----------ESTO SIRVE PARA METER ESTOS WIDGETS SOLAMENTE A QGROUP PANEL------------

        self.panelHorizontalp = QHBoxLayout() #crea la caja horizontal

        self.panelHorizontalp.addWidget(self.lista1) #mete la lista vertical items
        self.panelHorizontalp.addLayout(self.cajaVerticalBotones) #mete la lista vertical radiobuton

        self.grupoPanel.setLayout(self.panelHorizontalp) #este layout se mete completo dentro del QGroupBox("Panel")
# ---------------------------------------------------------------------------------------


# -----------PARA ORGANIZAR TODOS LOS WIDGETS EN UNA TABLA------------

        self.grid = QGridLayout() #crear una tabla para poder ajustar todo

        self.grid.addWidget(self.grupoPanel, 0, 0) #aqui va el grupo Panel donde metimos los items y el radio buton
        self.grid.addLayout(self.vertical,1,0) #aqui va el texto, contraseña y la lista extendida
        self.grid.addWidget(self.pestaña,0,1) #aqui va las pestañas que contiene los checkboxes y el slider
        self.grid.addWidget(self.espacioTexto,1,1) #el cuador de texto grande

        self.setLayout(self.grid) #esto signfica que la ventana usara esta cuadricula como su organizacion principal
# ----------------------------------------------------------------------



    def primerPanelButtons(self):
        self.r1btn = QRadioButton("RadioButton1")
        self.r2btn = QRadioButton("RadioButton2")
        self.r3btn = QRadioButton("RadioButton3")
        self.r4btn = QRadioButton("InactiveRadio")
        self.pusarBtn = QPushButton("Button")

        self.r4btn.setEnabled(False)

        self.cajaVerticalBotones = QVBoxLayout()
        self.cajaVerticalBotones.addWidget(self.r1btn)
        self.cajaVerticalBotones.addWidget(self.r2btn)
        self.cajaVerticalBotones.addWidget(self.r3btn)
        self.cajaVerticalBotones.addWidget(self.r4btn)
        self.cajaVerticalBotones.addWidget(self.pusarBtn)




    def primerPanelList(self):
        self.modelo = QStandardItemModel()
        self.lista1 = QListView()
        self.item1 = QStandardItem("Item 1")
        self.item2 = QStandardItem("Item 2")
        self.item3 = QStandardItem("Item 3")
        self.item4 = QStandardItem("Item 4")
        self.item5 = QStandardItem("Item 5")

        self.modelo.appendRow(self.item1)
        self.modelo.appendRow(self.item2)
        self.modelo.appendRow(self.item3)
        self.modelo.appendRow(self.item4)
        self.modelo.appendRow(self.item5)

        self.lista1.setModel(self.modelo)



    def paneles(self):
        self.labelParaEscribir = QLineEdit("TextField")
        self.labelContrasena = QLineEdit()
        self.desplegable = QComboBox()
        self.desplegable.addItems(["Item 1", "Item 2","Item 3","Item 4","Item 5"])
        self.labelContrasena.setEchoMode(QLineEdit.EchoMode.Password)

        self.vertical = QVBoxLayout()

        self.vertical.addWidget(self.labelParaEscribir)
        self.vertical.addWidget(self.labelContrasena)
        self.vertical.addWidget(self.desplegable)

    def pestañas(self):
        self.pestaña = QTabWidget()
        self.tab1 = QWidget()  # contenido de la pestaña

        self.casilla1 = QCheckBox("UncheckedCheckBox")
        self.casilla2 = QCheckBox("CheckedCheckBox")
        self.casilla2.setChecked(True)
        self.casilla3 = QCheckBox("InactiveCheckBox")
        self.casilla3.setEnabled(False)
        self.deslizador = QSlider(Qt.Orientation.Horizontal)

        self.cajaVertical = QVBoxLayout()
        self.cajaVertical.addWidget(self.casilla1)
        self.cajaVertical.addWidget(self.casilla2)
        self.cajaVertical.addWidget(self.casilla3)
        self.cajaVertical.addWidget(self.deslizador)


        self.tab1.setLayout(self.cajaVertical)
        self.pestaña.addTab(self.tab1, "SelectTab")
        self.tab2 = QWidget()  # contenido de la pestaña
        self.pestaña.addTab(self.tab2, "OtherTab")








if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaCopia()
    sys.exit(app.exec())