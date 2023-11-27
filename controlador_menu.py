from PyQt5.QtWidgets import QApplication,QMessageBox
from vista_menu import VistaLogin, VistaPrincipal
from menu_model import ModeloMenu
from main_dicom import main_dicom
from main_mat import main_mat
from main_png import main_png
from main_csv import mainCSV

class Controlador:
    def __init__(self, modelo):
        self.modelo = modelo
        self.app = QApplication([])
        self.vista_login = VistaLogin(self)
        self.vista_principal = None

    def verificar_credenciales(self):
        usuario = self.vista_login.entry_usuario.text()
        contraseña = self.vista_login.entry_contraseña.text()

        if usuario in self.modelo.usuarios and self.modelo.usuarios[usuario] == contraseña:
            self.vista_login.close()
            self.mostrar_vista_principal()
        else:
            QMessageBox.critical(self.vista_login, "Error", "Credenciales incorrectas")

    def mostrar_vista_principal(self):
        self.vista_principal = VistaPrincipal(self)
        self.vista_principal.show()

    def mat(self):
        mat_window = main_mat()
        mat_window.show()

    def png(self):
        main_png()

    def dicom(self):
        dicom_window = main_dicom()
        dicom_window.show()

    def csv(self):
        csv_window = mainCSV()
        csv_window.show()


if __name__ == "__main__":
    modelo = ModeloMenu()
    controlador = Controlador(modelo)
    controlador.vista_login.show()
    controlador.app.exec_()