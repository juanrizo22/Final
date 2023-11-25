import sys
from PyQt5.QtWidgets import QApplication
from model import MatModel
from view import MatView
from controller import MatController

def main_mat():
    app = QApplication(sys.argv)

    modelo = MatModel()
    vista = MatView()
    controlador = MatController(modelo, vista)
    vista.set_controller(controlador)
    vista.init_ui()
    vista.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main_mat()