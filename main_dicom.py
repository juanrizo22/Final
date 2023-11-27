import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from vista_dicom import Vista
from modelo_dicom import basededatos
from controlador_dicom import Coordinador
def main_dicom():

    mi_vista = Vista()
    mi_modelo = basededatos()
    mi_coordinador = Coordinador(mi_vista, mi_modelo)
    mi_vista.setCoordinador(mi_coordinador)
    mi_vista.setup()
    return mi_vista

if __name__ == "__main__":
    app=QApplication(sys.argv)
    main_window=QMainWindow()
    main_dicom_window=main_dicom()
    main_window.setCentralWidwet(main_dicom_window)
    main_window.show()
    sys.exit(app.exec_())
