from modelo_csv import CSVModel
from vista_csv import VentanaCSV
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from controller_csv import Coordinador

def mainCSV():
    mi_modelo = CSVModel()
    mi_vista = VentanaCSV()
    mi_coordinador = Coordinador(mi_vista, mi_modelo)
    mi_vista.setCoordinador(mi_coordinador)
    return mi_vista

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_mat_window = mainCSV()
    main_window.setCentralWidget(main_mat_window)
    main_window.show()
    sys.exit(app.exec_())
