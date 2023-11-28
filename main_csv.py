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
    return mi_vista  # Devuelve la instancia de VentanaCSV

if __name__ == "__main__":
    csv_window = mainCSV()
    csv_window.show()
    sys.exit(csv_window.app.exec_())
