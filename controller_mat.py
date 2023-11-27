import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import os

class MatController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.controller = self
    

    def load_mat_file(self):
        if self.view is not None:  
            file_dialog = QFileDialog()
            print(type(self.view))
            file_path, _ = file_dialog.getOpenFileName(self.view, "Abrir archivo MAT", "", "MAT Files (*.mat)")

            if file_path:
                if self.model.load_mat_file(file_path):
                    keys = [str(key) for key in self.model.mat_data.keys() if not key.startswith('__')]
                    self.view.key_combo_box.addItems(keys)

    def plot_channel(self):
        if self.model.mat_data is None:
            QMessageBox.warning(self.view, "Advertencia", "Por favor, carga un archivo MAT primero.")
            return

        selected_key = self.view.key_combo_box.currentText()

        try:
            data = self.model.mat_data[selected_key]
            channel_index = self.view.channel_spin_box.value()

            if not isinstance(data, np.ndarray) or data.ndim < 2 or channel_index >= data.shape[0]:
                QMessageBox.warning(self.view, "Advertencia", "No es un arreglo válido o el canal seleccionado no existe.")
                return

            channel_data = data[channel_index, :]

            plt.figure()
            plt.plot(channel_data)
            plt.title("Grafico del Canal")
            plt.xlabel("Muestras")
            plt.ylabel("Amplitud")

            # Guardar la imagen en un archivo temporal
            image_path = "temp_plot.png"
            plt.savefig(image_path)

            # Mostrar la imagen en el QLabel
            self.view.show_image(image_path)

            # Eliminar el archivo temporal después de mostrar la imagen
            os.remove(image_path)

        except Exception as e:
            QMessageBox.critical(self.view, "Error", f"Error al graficar: {str(e)}")
        
