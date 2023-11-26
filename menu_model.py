import json
class ModeloMenu:
    def __init__(self):
        self.usuarios = self.cargar_usuarios()

    def cargar_usuarios(self):
        try:
            with open("usuarios.json", "r") as file:
                usuarios = json.load(file)
            return usuarios
        except FileNotFoundError:
            return {}