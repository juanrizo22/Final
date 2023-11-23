from PyQt5.QtWidgets import QMainWindow, QFileDialog, QComboBox, QMessageBox, QLabel, QPushButton, QSpinBox, QGraphicsView
from PyQt5.QtWidgets import QGraphicsScene  

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MatView(QMainWindow):
    def __init__(self):
        super(MatView, self).__init__()
        self.controller = None

    def set_controller(self, c):
        self.controller = c

    def init_ui(self):
        self.setWindowTitle("MAT File Viewer")
        self.setGeometry(100, 100, 800, 600)

        # ComboBox para las llaves
        self.key_combo_box = QComboBox(self)
        self.key_combo_box.setGeometry(10, 10, 200, 30)

        # Botón para cargar archivo MAT
        load_button = QPushButton("Cargar MAT", self)
        load_button.setGeometry(220, 10, 150, 30)
        load_button.clicked.connect(self.controller.load_mat_file)

        # SpinBox para seleccionar el canal
        channel_label = QLabel("Canal:", self)
        channel_label.setGeometry(400, 10, 50, 30)

        self.channel_spin_box = QSpinBox(self)
        self.channel_spin_box.setGeometry(450, 10, 50, 30)

        # Botón para graficar
        plot_button = QPushButton("Graficar", self)
        plot_button.setGeometry(520, 10, 100, 30)
        plot_button.clicked.connect(self.controller.plot_channel)

        # QGraphicsView y escena para mostrar la gráfica
        self.graphics_view = QGraphicsView(self)
        self.graphics_view.setGeometry(10, 50, 780, 500)
        self.graphics_scene = QGraphicsScene()
        self.graphics_view.setScene(self.graphics_scene)

    def plot_graph(self, x, y, title, xlabel, ylabel):
        # Limpia la escena antes de mostrar una nueva gráfica
        self.graphics_scene.clear()

        # Crear la gráfica usando Matplotlib
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        # Convertir la gráfica de Matplotlib a QPixmap
        canvas = FigureCanvas(fig)
        canvas.draw()
        pixmap = canvas.toPixmap()

        # Mostrar QPixmap en QGraphicsScene
        self.graphics_scene.addPixmap(pixmap)

        # Liberar la memoria
        plt.close(fig)