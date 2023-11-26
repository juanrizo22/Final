import tkinter as tk
from tkinter import messagebox
from vista_menu import VistaLogin, VistaPrincipal
from menu_model import ModeloMenu
from main_dicom import main_dicom
from main_mat import main_mat
from main_png import main_png

class Controlador:
    def __init__(self, modelo):
        self.modelo = modelo
        self.vista_login = VistaLogin(self)
        self.vista_principal = None

    def verificar_credenciales(self):
        usuario = self.vista_login.entry_usuario.get()
        contraseña = self.vista_login.entry_contraseña.get()

        if usuario in self.modelo.usuarios and self.modelo.usuarios[usuario] == contraseña:
            self.vista_login.destroy()
            self.mostrar_vista_principal()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    def mostrar_vista_principal(self):
        self.vista_principal = VistaPrincipal(self)

    def mat(self):
        main_mat()
    
    def png(self):
        main_png()
    
    def dicom(self):
        main_dicom()
    
    def csv(self):
        pass


if __name__ == "__main__":
    modelo = ModeloMenu()
    controlador = Controlador(modelo)
    controlador.vista_login.mainloop()