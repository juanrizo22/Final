import sys
import os
import pandas as pd
from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox, QFileDialog, QVBoxLayout, QWidget
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MyGraphCanvas(QWidget):
    def __init__(self, parent=None, width=6, height=5, dpi=100):
        super().__init__(parent)

        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        
        self.canvas = FigureCanvas(self.fig)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def graficar(self, dataframe, columna_x, columna_y):
        if not dataframe.empty:
            self.axes.clear()
            self.axes.bar(dataframe[columna_x], dataframe[columna_y])
            self.axes.set_xlabel(columna_x)
            self.axes.set_ylabel(columna_y)
            self.canvas.draw()
        else:
            print("No hay datos para graficar.")
class VentanaCSV(QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("csv.ui", self)
        self.setup()

    def setup(self):
        self.layout = QVBoxLayout()
        self.grafico.setLayout(self.layout)
        self.sc = MyGraphCanvas()
        self.layout.addWidget(self.sc)

        self.MediaBotton.clicked.connect(self.mean)
        self.MedianaButton.clicked.connect(self.median)
        self.LoadButton.clicked.connect(self.load)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.close)
        self.comboBox_eje_x.currentIndexChanged.connect(self.axisX)
        self.comboBox_eje_y.currentIndexChanged.connect(self.axisY)
        self.combo_segmento_x.setValidator(QRegExpValidator(QRegExp("[0-9]+")))
        self.combo_segmento_y.setValidator(QRegExpValidator(QRegExp("[0-9]+")))

    def init_plot(self):
        # Crea la instancia de MyGraphCanvas y agrega al widget grafico
        self.graph_canvas = MyGraphCanvas(self.grafico)
        layout = QVBoxLayout()
        layout.addWidget(self.graph_canvas)
        self.grafico.setLayout(layout)

    def mean(self):
        try:
            columna = self.comboBox_eje_y.currentText()

            if self.__coordinador.validar_numeros(columna):
                media = self.__coordinador.calcular_media(columna)

                self.datos.setText(f"La media de {columna} es: {media}")
            else:
                self.datos.setText(f"Error: La columna {columna} no tiene números.")
        except TypeError:
            QMessageBox.warning(self, "Advertencia", "Elija un archivo antes de hacer operaciones.")

    def median(self):
        try:
            columna = self.comboBox_eje_y.currentText()

            if self.__coordinador.validar_numeros(columna):
                mediana = self.__coordinador.calcular_mediana(columna)

                self.datos.setText(f"La mediana de {columna} es: {mediana}")
            else:
                self.datos.setText(f"Error: La columna {columna} no tiene números.")

        except TypeError:
            QMessageBox.warning(self, "Advertencia", "Elija un archivo antes de hacer operaciones.")

    def load(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Abrir archivo CSV", "", "CSV Files (*.csv);;All Files (*)")

        if file_name:
            try:
                # Llama a la función para leer el archivo CSV y graficar todos los segmentos
                self.__coordinador.getfile(file_name)
                self.__coordinador.graficar_todo()
                self.actualizar_nombres_columnas()  # Actualiza los nombres de las columnas en los ComboBox
            except AttributeError:
                pass
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Advertencia", f"Error al procesar el archivo: {e}")



    def accept(self):
        try:
            columna_x = self.comboBox_eje_x.currentText()
            columna_y = self.comboBox_eje_y.currentText()

            if columna_x and columna_y:
                dataframe = self.__coordinador.getdataframe()
                self.actualizar_nombres_columnas()
                self.sc.axes.clear()

                # Obtener los valores de los segmentos desde los QLineEdit
                min_x = float(self.combo_segmento_x.text())
                max_x = float(self.combo_segmento_y.text())

                if min_x <= max_x:
                    # Filtrar el DataFrame según los valores del segmento
                    segmento_data = dataframe[(dataframe[columna_x] >= min_x) & (dataframe[columna_x] <= max_x)]
                    
                    # Graficar el segmento filtrado
                    self.sc.axes.bar(segmento_data[columna_x], segmento_data[columna_y])
                    self.sc.axes.set_xlabel(columna_x)
                    self.sc.axes.set_ylabel(columna_y)
                    self.sc.canvas.draw()
                else:
                    print("Los valores del segmento no son válidos.")
            else:
                QMessageBox.warning(self, "Advertencia", "Seleccione columnas válidas para los ejes X e Y.")
        except ValueError:
            pass
        except Exception as e:
            QMessageBox.warning(self, "Advertencia", f"Error: {e}")


    def close(self):
        self.hide()

    def actualizar_nombres_columnas(self):
        # Obtén los nombres de las columnas del modelo
        columnas = self.__coordinador.getcolumnas()

        if columnas is not None:
            # Limpiar ambos ComboBox
            self.comboBox_eje_x.clear()
            self.comboBox_eje_y.clear()

            # Llena ambos ComboBox con los nombres de las columnas
            for columna in columnas:
                self.comboBox_eje_x.addItem(columna)
                self.comboBox_eje_y.addItem(columna)
        else:
            QMessageBox.warning(self, "Advertencia", "No se puede cargar el archivo debido a que no tiene los datos buenos.")

    def axisX(self):
        columna_seleccionada_x = self.comboBox_eje_x.currentText()
        self.comboBox_eje_y.removeItem(self.comboBox_eje_y.findText(columna_seleccionada_x))

    def axisY(self):
        columna_seleccionada_y = self.comboBox_eje_y.currentText()
        self.comboBox_eje_x.removeItem(self.comboBox_eje_x.findText(columna_seleccionada_y))

    def setCoordinador(self, c):
        self.__coordinador = c
