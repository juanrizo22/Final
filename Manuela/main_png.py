from view_png import PNGView
from model_png import PNGModel
from controller_png import PNGController
import tkinter as tk

if __name__ == "__main__":
    model = PNGModel()
    root = tk.Tk()
    controller = PNGController(root, model, None)
    root.mainloop()