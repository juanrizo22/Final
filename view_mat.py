from PyQt5.QtWidgets import QMainWindow,  QComboBox,  QLabel, QPushButton, QSpinBox
from PyQt5.QtGui import QPixmap

class MatView(QMainWindow):
    def __init__(self):
        super(MatView, self).__init__()
        self.controller = None

        self.setWindowTitle("MAT File Viewer")
        self.setGeometry(100, 100, 800, 900)
        self.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.image_label = QLabel(self)
        self.image_label.setGeometry(10, 50, 780, 800)

    def set_controller(self,c):
        self.controller=c

        
    def init_ui(self):
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

        # Botón para cerrar la ventana actual
        close_button = QPushButton("Cerrar", self)
        close_button.setGeometry(640, 10, 100, 30)
        close_button.clicked.connect(self.closeEvent)
    
    def show_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)
        self.image_label.show()

    def closeEvent(self):
      self.hide()
