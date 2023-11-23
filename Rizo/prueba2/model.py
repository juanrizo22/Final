import scipy.io

class MatModel:
    def __init__(self):
        self.mat_data = None

    def load_mat_file(self, file_path):
        try:
            self.mat_data = scipy.io.loadmat(file_path)
            return True
        except Exception as e:
            print(f"No se pudo cargar el archivo MAT: {str(e)}")
            return False