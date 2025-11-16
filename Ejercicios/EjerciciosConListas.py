import sys
from PyQt6.QtWidgets import QVBoxLayout, QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, \
    QGridLayout


class EjercicioConListas(QMainWindow):
    def __init__(self):
        super().__init__()

        caixaV= QVBoxLayout()

        txtCadro1 = QLineEdit()
        txtCadro2 = QLineEdit()
        cmbCombo = QComboBox()

        cmbCombo.addItems( ["Opción 1", "Opción 2", "Opción 3", "Opción 4"] )


        caixaV.addWidget(txtCadro1)
        caixaV.addWidget(txtCadro2)
        caixaV.addWidget(cmbCombo)

        maia = QGridLayout()

        maia.addLayout(caixaV, 1, 0,1,1)
        container = QWidget()

        container.setLayout(maia)
        self.setCentralWidget(container)
        self.show()
        # metodo currentTextChanged
        # Metodo ItemTextChanged
        # setplainText



if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = EjercicioConListas()
    fiestra.show()
    sys.exit(aplicacion.exec())