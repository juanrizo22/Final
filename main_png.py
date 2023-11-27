from model_png import PNGModel
from controller_png import PNGController
import tkinter as tk

def main_png():
    model = PNGModel()
    root = tk.Tk()
    controller = PNGController(root, model, None)
    root.mainloop()
