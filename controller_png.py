
from tkinter import filedialog
from view_png import PNGView

class PNGController:
    def __init__(self, root, model, view):
        self.root = root
        self.model = model
        self.view = view
        if self.view is None:
            self.view =PNGView(root, self)

    def cargar_imagen(self):
        ruta_imagen = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.jpg;*.png")])
        if ruta_imagen:
            self.model.cargar_imagen(ruta_imagen)
            self.view.mostrar_imagen(self.model.imagen_original)

    def actualizar_tamano_kernel(self, valor):
        self.model.tamano_kernel = int(valor)

    def aplicar_operacion(self, operacion):
        self.model.aplicar_operacion_morfologica(operacion)
        self.view.mostrar_imagen(self.model.imagen_procesada)


