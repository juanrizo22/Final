import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class AplicacionMorfologica:
    def __init__(self, ventana, titulo):
        self.ventana = ventana
        self.ventana.title(titulo)

        # Personalizar la apariencia de la ventana
        self.ventana.configure(bg='pink')  # Fondo rosado

        # Variables para la ruta de la imagen, el tamaño del kernel y la imagen
        self.ruta_imagen = None
        self.tamano_kernel = 1  # Tamaño inicial del kernel
        self.imagen_original = None

        # Botón para cargar imagen
        btn_cargar = tk.Button(ventana, text="Cargar Imagen", command=self.cargar_imagen)
        btn_cargar.pack(pady=10)

        # Control deslizante para ajustar el tamaño del kernel
        lbl_tamano_kernel = tk.Label(ventana, text="Tamaño del Kernel:", bg='pink', font=('Arial', 14))
        lbl_tamano_kernel.pack()
        sld_tamano_kernel = tk.Scale(ventana, from_=1, to=30, orient="horizontal", command=self.actualizar_tamano_kernel)
        sld_tamano_kernel.set(self.tamano_kernel)
        sld_tamano_kernel.pack()

        # Etiqueta para mostrar las dimensiones de la imagen
        self.lbl_dimensiones = tk.Label(ventana, text="", bg='pink', font=('Arial', 14))
        self.lbl_dimensiones.pack()

        # Botones para aplicar operaciones morfológicas
        btn_erosion = tk.Button(ventana, text="Erosión", command=lambda: self.aplicar_operacion("erosion"))
        btn_erosion.pack(pady=5)

        btn_dilatacion = tk.Button(ventana, text="Dilatación", command=lambda: self.aplicar_operacion("dilatacion"))
        btn_dilatacion.pack(pady=5)

        btn_cierre = tk.Button(ventana, text="Cierre", command=lambda: self.aplicar_operacion("cierre"))
        btn_cierre.pack(pady=5)

        btn_apertura = tk.Button(ventana, text="Apertura", command=lambda: self.aplicar_operacion("apertura"))
        btn_apertura.pack(pady=5)

    def cargar_imagen(self):
        self.ruta_imagen = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.jpg;*.png")])
        if self.ruta_imagen:
            self.imagen_original = cv2.imread(self.ruta_imagen)
            self.mostrar_imagen(self.imagen_original)

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
            self.lbl_imagen = tk.Label(self.ventana, image=imagen_tk, bg='pink')
            self.lbl_imagen.image = imagen_tk
            self.lbl_imagen.pack()

        # Mostrar las dimensiones de la imagen
        dimensiones = f"Dimensiones: {imagen.shape[1]} x {imagen.shape[0]}"
        self.lbl_dimensiones.configure(text=dimensiones)

    def actualizar_tamano_kernel(self, valor):
        self.tamano_kernel = int(valor)

    def aplicar_operacion(self, tipo_operacion):
        if self.imagen_original is not None:
            imagen_procesada = self.realizar_operacion_morfologica(self.imagen_original, tipo_operacion)
            self.mostrar_imagen(imagen_procesada)

    def realizar_operacion_morfologica(self, imagen, operacion):
        kernel = np.ones((self.tamano_kernel, self.tamano_kernel), np.uint8)

        if operacion == 'erosion':
            return cv2.erode(imagen, kernel, iterations=1)
        elif operacion == 'dilatacion':
            return cv2.dilate(imagen, kernel, iterations=1)
        elif operacion == 'cierre':
            return cv2.morphologyEx(imagen, cv2.MORPH_CLOSE, kernel, iterations=2)
        elif operacion == 'apertura':
            return cv2.morphologyEx(imagen, cv2.MORPH_OPEN, kernel, iterations=2)
        else:
            return imagen

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionMorfologica(root, "Aplicación Morfológica")
    root.mainloop()






