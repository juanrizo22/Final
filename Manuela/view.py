import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2

class View:
    def __init__(self, root, controller):
        self.root = root
        self.root.title("Aplicación Morfológica")
        self.root.configure(bg='#FFAAFF')
        self.root.geometry("750x700") 
        self.controller = controller

        # Botón para cargar imagen
        self.btn_cargar = tk.Button(root, text="Cargar Imagen", command=self.controller.cargar_imagen, bg='white', fg='black')
        self.btn_cargar.pack(pady=10)

        # Control deslizante para ajustar el tamaño del kernel
        self.lbl_tamano_kernel = tk.Label(root, text="Tamaño del Kernel:", bg='#FFAAFF', font=('Arial', 14))
        self.lbl_tamano_kernel.pack()
        self.sld_tamano_kernel = tk.Scale(root, from_=1, to=30, orient="horizontal", command=self.controller.actualizar_tamano_kernel, bg='#FFAAFF', length=200, troughcolor='#FF69B4', sliderlength=15)
        self.sld_tamano_kernel.set(self.controller.model.tamano_kernel)
        self.sld_tamano_kernel.pack()

        # Etiqueta para mostrar las dimensiones de la imagen
        self.lbl_dimensiones = tk.Label(root, text="", bg='blue', fg='white', font=('Arial', 14))
        self.lbl_dimensiones.pack()

        # Botones para aplicar operaciones morfológicas
        self.btn_erosion = tk.Button(root, text="Erosión", command=lambda: self.controller.aplicar_operacion("erosion"), bg='white', fg='black')
        self.btn_erosion.pack(pady=5)

        self.btn_dilatacion = tk.Button(root, text="Dilatación", command=lambda: self.controller.aplicar_operacion("dilatacion"), bg='white', fg='black')
        self.btn_dilatacion.pack(pady=5)

        self.btn_cierre = tk.Button(root, text="Cierre", command=lambda: self.controller.aplicar_operacion("cierre"), bg='white', fg='black')
        self.btn_cierre.pack(pady=5)

        self.btn_apertura = tk.Button(root, text="Apertura", command=lambda: self.controller.aplicar_operacion("apertura"), bg='white', fg='black')
        self.btn_apertura.pack(pady=5)

    def mostrar_imagen(self, imagen):
        imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        imagen_pil = Image.fromarray(imagen_rgb)
        imagen_tk = ImageTk.PhotoImage(imagen_pil)

        # Si ya hay una etiqueta de imagen, actualizarla
        if hasattr(self, 'lbl_imagen'):
            self.lbl_imagen.configure(image=imagen_tk)
            self.lbl_imagen.image = imagen_tk
        else:
            # Si no, crear una nueva etiqueta de imagen
            self.lbl_imagen = tk.Label(self.root, image=imagen_tk, bg='#FF69B4')
            self.lbl_imagen.image = imagen_tk
            self.lbl_imagen.pack()

        # Mostrar las dimensiones de la imagen
        dimensiones = f"Dimensiones: {imagen.shape[1]} x {imagen.shape[0]}"
        self.lbl_dimensiones.configure(text=dimensiones, bg='white', fg='black')

