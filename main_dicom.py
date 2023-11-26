import sys
from PyQt5.QtWidgets import QApplication
from vista_dicom import Ventanainicio
from modelo_dicom import basededatos
from controlador_dicom import Coordinador
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