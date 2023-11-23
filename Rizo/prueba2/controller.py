import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from model import MatModel
from view import MatView

class MatController:
    def __init__(self, model):
        self.model = model
        self.view = None

    def set_view(self, view):
        self.view = view

    def load_mat_file(self):
        file_dialog = QFileDialog()
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

            # Llama a la función para mostrar la gráfica en el QGraphicsView
            self.view.plot_graph(
                x=np.arange(len(channel_data)),
                y=channel_data,
                title="Grafico del Canal",
                xlabel="Muestras",
                ylabel="Amplitud"
            )

        except Exception as e:
            QMessageBox.critical(self.view, "Error", f"Error al graficar: {str(e)}")