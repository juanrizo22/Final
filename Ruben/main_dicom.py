import sys
from PyQt5.QtWidgets import QApplication
from vista import Ventanainicio
from modelo import basededatos
from controlador import Coordinador
def main_dicom():

    app = QApplication(sys.argv)
    mi_vista = Ventanainicio()
    mi_modelo = basededatos()
    mi_coordinador = Coordinador(mi_vista, mi_modelo)
    mi_vista.setCoordinador(mi_coordinador)
    mi_vista.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main_dicom()