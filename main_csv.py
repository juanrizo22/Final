from modelo_csv import CSVModel
from vista_csv import VentanaCSV
import sys
from PyQt5.QtWidgets import QApplication
from controller_csv import Coordinador

def mainCSV():
    app = QApplication(sys.argv)
    mi_modelo = CSVModel()
    mi_vista = VentanaCSV()
    mi_coordinador = Coordinador(mi_vista, mi_modelo)
    mi_vista.setCoordinador(mi_coordinador)
    mi_vista.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    mainCSV()
