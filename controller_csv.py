
from modelo_csv import CSVModel
from vista_csv import VentanaCSV
import sys
from PyQt5.QtWidgets import QApplication

class Coordinador(object):
    def __init__(self, vista, modelo):
        self.__mi_vista = vista
        self.__mi_modelo = modelo

    def getfile(self, file):
        try:
            dataframe = self.__mi_modelo.leer_csv(file)
            # return dataframe
        except FileNotFoundError:
            return None
        except Exception as e:
            return None
        
    def getdataframe(self):
        return self.__mi_modelo.gettablaex()



    def validar_numeros(self, columna):
        try:
            self.__mi_modelo.gettablaex()[columna].astype(float)
            return True
        except ValueError:
            return False

    def calcular_media(self, columna):
        return self.__mi_modelo.media(columna)
    
    def getcolumnas(self):
        return self.__mi_modelo.getcolumnas()
        
    def calcular_mediana(self, columna):
            return self.__mi_modelo.mediana(columna)
    
    def graficar_todo(self):
        try:
            dataframe = self.getdataframe()

            if dataframe is not None and not dataframe.empty:
                columna_x = dataframe.columns[0]  # Tomar la primera columna como eje X
                columna_y = dataframe.columns[1]  # Tomar la segunda columna como eje Y
                
                self.__mi_vista.sc.graficar(dataframe, columna_x, columna_y)

        except Exception as e:
            print(f"Error al graficar todos los segmentos: {e}")


    
