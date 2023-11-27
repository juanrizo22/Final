import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

class CSVModel:
    def __init__(self):
        # super().__init__()
        self.__tablaEx = pd.DataFrame(None)
        self.__columnas = self.__tablaEx.columns
        self.__shape = self.__tablaEx.shape

    def gettablaex(self):
        return self.__tablaEx

    def getcolumnas(self):
        return self.__columnas

    def getshape(self):
        return self.__shape

    def leer_csv(self, path):
        if os.path.exists(path):
            self.__tablaEx = pd.read_csv(path)
            self.__columnas = self.__tablaEx.columns
            self.__shape = self.__tablaEx.shape
            # return self.__tablaEx  # Return the DataFrame
        else:
            return None
        
        
    def mediana (self,columna):
        return self.__tablaEx[columna].astype(float).median()
    
    def media (self,columna):
        return self.__tablaEx[columna].astype(float).mean()
    
    def graficar_todo(self):
        if not self.__tablaEx.empty:
            # Graficar todos los segmentos
            self.__tablaEx.plot(kind='bar', legend=False)
            plt.xlabel("Eje X")
            plt.ylabel("Eje Y")
            plt.show()
        else:
            print("No hay datos para graficar.")





