import cv2
import numpy as np

class PNGModel:
    def __init__(self):
        self.ruta_imagen = None
        self.tamano_kernel = 1
        self.imagen_original = None
        self.imagen_procesada = None

    def cargar_imagen(self, ruta_imagen):
        self.ruta_imagen = ruta_imagen
        self.imagen_original = cv2.imread(self.ruta_imagen)

    def aplicar_operacion_morfologica(self, operacion):
        if self.imagen_original is not None:
            kernel = np.ones((self.tamano_kernel, self.tamano_kernel), np.uint8)

            if operacion == 'erosion':
                self.imagen_procesada = cv2.erode(self.imagen_original, kernel, iterations=1)
            elif operacion == 'dilatacion':
                self.imagen_procesada = cv2.dilate(self.imagen_original, kernel, iterations=1)
            elif operacion == 'cierre':
                self.imagen_procesada = cv2.morphologyEx(self.imagen_original, cv2.MORPH_CLOSE, kernel, iterations=2)
            elif operacion == 'apertura':
                self.imagen_procesada = cv2.morphologyEx(self.imagen_original, cv2.MORPH_OPEN, kernel, iterations=2)
            else:
                self.imagen_procesada = self.imagen_original
