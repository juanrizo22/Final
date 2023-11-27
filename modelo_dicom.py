import pydicom 
import mysql.connector
from PyQt5.QtCore import QObject
import matplotlib.pyplot as plt
import os
class basededatos(QObject):

    def get_path(self, f): 
        self.__carpeta = f

    def picture_creator(self, imagen):
        ds = pydicom.dcmread(self.__carpeta+'/'+imagen)
        pixel_data = ds.pixel_array

        if len(pixel_data.shape) == 3:
            slice_index = pixel_data.shape[0] // 2
            selected_slice = pixel_data[slice_index, :, :]
            plt.imshow(selected_slice, cmap=plt.cm.bone)
        else:

            plt.imshow(pixel_data, cmap=plt.cm.bone)

        plt.axis('off')
        plt.savefig("temp_image.png")

    def obtener_informacion_paciente(self, imagen):
        # Ruta completa del archivo DICOM
        ruta_completa = os.path.join(self.__carpeta, imagen)

        # Leer el archivo DICOM
        ds = pydicom.dcmread(ruta_completa)

        # Obtener información del paciente
        nombre_paciente = ds.PatientName
        id_paciente = ds.PatientID
        fecha_nacimiento = ds.PatientBirthDate
        sexo = ds.PatientSex

        # Puedes agregar más campos según lo que necesites

        # Crear un diccionario con la información del paciente
        info_paciente = {
            'Nombre': str(nombre_paciente),
            'ID': str(id_paciente),
            'Fecha de Nacimiento': str(fecha_nacimiento),
            'Sexo': str(sexo),
            # Agregar más campos si es necesario
        }

        return info_paciente
    
class MySQL:

    def conectar_bd(self):
        try:
            conexion = mysql.connector.connect(
                host='localhost',
                user='informatica2',
                password='bio123',
                database='informatica2'
            )
            print("Conexión exitosa a la base de datos")
            return conexion
        except mysql.connector.Error as err:
            print(f"No se pudo conectar: {err}")
            return None

    def crear_tabla(self):
        try:
            conexion = self.conectar_bd()
            if conexion:
                cursor = conexion.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS pacientes (lote INT PRIMARY KEY, nombre VARCHAR(100), ID VARCHAR(100), fecha_nacimiento DATE, sexo VARCHAR(10))")
                conexion.commit()
                cursor.close()
                conexion.close()
        except mysql.connector.Error as err:
            print(f"Error al crear la tabla: {err}")

    def insertar_paciente(self, info_paciente):
        try:
            conexion = self.conectar_bd()
            if conexion:
                cursor = conexion.cursor()
                consulta = "INSERT INTO pacientes (nombre, ID, fecha_nacimiento, sexo) VALUES (%s, %s, %s, %s)"
                datos = (info_paciente['Nombre'], info_paciente['ID'], info_paciente['Fecha de Nacimiento'], info_paciente['Sexo'])
                cursor.execute(consulta, datos)
                conexion.commit()
                cursor.close()
                conexion.close()
                print("Paciente insertado correctamente")
        except mysql.connector.Error as err:
            print(f"Error al insertar paciente en la base de datos: {err}")

    
