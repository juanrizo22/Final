from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class VistaLogin(QWidget):
    def __init__(self, controlador):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 500, 300)
        self.setStyleSheet("background-color: rgb(255, 170, 255);")

        self.controlador = controlador

        self.label_usuario = QLabel("Usuario:")
        self.entry_usuario = QLineEdit()
        self.label_contraseña = QLabel("Contraseña:")
        self.entry_contraseña = QLineEdit()
        self.entry_contraseña.setEchoMode(QLineEdit.Password)

        self.boton_ingresar = QPushButton("Ingresar")
        self.boton_ingresar.clicked.connect(self.controlador.verificar_credenciales)

        layout = QVBoxLayout()
        layout.addWidget(self.label_usuario)
        layout.addWidget(self.entry_usuario)
        layout.addWidget(self.label_contraseña)
        layout.addWidget(self.entry_contraseña)
        layout.addWidget(self.boton_ingresar)

        self.setLayout(layout)


class VistaPrincipal(QWidget):
    def __init__(self, controlador):
        super().__init__()

        self.setWindowTitle("Principal")
        self.setGeometry(100, 100, 500, 300)
        self.setStyleSheet("background-color: rgb(255, 170, 255);")

        self.controlador = controlador

        self.boton_mat = QPushButton("Abrir mat")
        self.boton_mat.clicked.connect(self.controlador.mat)

        self.boton_dicom = QPushButton("Abrir Dicom")
        self.boton_dicom.clicked.connect(self.controlador.dicom)

        self.boton_img = QPushButton("Abrir PNG")
        self.boton_img.clicked.connect(self.controlador.png)

        self.boton_csv = QPushButton("Abrir CSV")
        self.boton_csv.clicked.connect(self.controlador.csv)

        self.boton_salir = QPushButton("Salir")
        self.boton_salir.clicked.connect(self.salir)

        layout = QVBoxLayout()
        layout.addWidget(self.boton_mat)
        layout.addWidget(self.boton_dicom)
        layout.addWidget(self.boton_img)
        layout.addWidget(self.boton_csv)
        layout.addWidget(self.boton_salir)

        self.setLayout(layout)

    def salir(self):
        respuesta = QMessageBox.question(self, "Salir", "¿Estás seguro de que quieres salir?", QMessageBox.Yes | QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            self.close()