import tkinter as tk
from tkinter import messagebox
class VistaLogin(tk.Tk):
    def __init__(self, controlador):
        super().__init__()

        self.title("Login")
        self.geometry("500x300")
        self.config(bg="pink")

        self.controlador = controlador

        self.label_usuario = tk.Label(self, text="Usuario:")
        self.label_usuario.pack()

        self.entry_usuario = tk.Entry(self)
        self.entry_usuario.pack()

        self.label_contraseña = tk.Label(self, text="Contraseña:")
        self.label_contraseña.pack()

        self.entry_contraseña = tk.Entry(self, show="*")
        self.entry_contraseña.pack()

        self.boton_ingresar = tk.Button(self, text="Ingresar", command=self.controlador.verificar_credenciales)
        self.boton_ingresar.pack()

class VistaPrincipal(tk.Tk):
    def __init__(self, controlador):
        super().__init__()

        self.title("Principal")
        self.geometry("500x300")
        self.config(bg="pink")

        self.controlador = controlador

        self.boton_mat = tk.Button(self, text="Abrir mat", command=self.controlador.mat)
        self.boton_mat.pack()

        self.boton_dicom = tk.Button(self, text="Abrir Dicom", command=self.controlador.dicom)
        self.boton_dicom.pack()

        self.boton_img = tk.Button(self, text="Abrir PNG", command=self.controlador.png)
        self.boton_img.pack()

        self.boton_csv = tk.Button(self, text="Abrir CSV", command=self.controlador.csv)
        self.boton_csv.pack()

        self.boton_salir = tk.Button(self, text="Salir", command=self.salir)
        self.boton_salir.pack()

    def salir(self):
        respuesta = messagebox.askquestion("Salir", "¿Estás seguro de que quieres salir?")
        if respuesta == "yes":
            self.destroy()