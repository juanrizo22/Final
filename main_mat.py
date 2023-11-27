import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from model_mat import MatModel
from view_mat import MatView
from controller_mat import MatController

def main_mat():
    modelo = MatModel()
    vista = MatView()
    controlador = MatController(modelo, vista)
    vista.set_controller(controlador)
    vista.init_ui()
    return vista

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_mat_window = main_mat()
    main_window.setCentralWidget(main_mat_window)
    main_window.show()
    sys.exit(app.exec_())

