from modelo_dicom import basededatos
from vista_dicom import Vista
import sys
from PyQt5.QtWidgets import QApplication

from modelo_dicom import basededatos, MySQL
from vista_dicom import Vista
import sys
from PyQt5.QtWidgets import QApplication

class Coordinador(object):
    def __init__(self, vista, modelo, db_modelo):
        self.__mi_vista = vista
        self.__mi_modelo = modelo
        self.__db_modelo = db_modelo  # Agregamos el modelo de base de datos

    def img_conextion(self, imagen):
        self.__mi_modelo.picture_creator(imagen)

    def get_file(self, filename):
        self.__mi_modelo.get_path(filename)

    def information(self, picture):
        return self.__mi_modelo.obtener_informacion_paciente(picture)

    def insertar_paciente_en_db(self, picture):
        
        info_paciente = self.information(picture)

        self.__db_modelo.crear_tabla()

        self.__db_modelo.insertar_paciente(info_paciente)
