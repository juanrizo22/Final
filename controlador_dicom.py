from modelo import basededatos
from vista import Vista
import sys
from PyQt5.QtWidgets import QApplication

class Coordinador(object):
    def __init__(self,vista,modelo):
        self.__mi_vista = vista
        self.__mi_modelo = modelo

    
    def img_conextion(self, imagen):
        
        self.__mi_modelo.picture_creator(imagen)
    
    def get_file(self,filename):
        self.__mi_modelo.get_path(filename)
    # def listfile(self,file):
    #     return self.__mi_modelo.verarchivos(file)
    def infomartion (self, picture):
        return self.__mi_modelo.obtener_informacion_paciente(picture)
