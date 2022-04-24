from tkinter import*
from vista import Ventana

class Controlador:
    def __init__(self, root):
        self.root_controller = root
        obj = Ventana(self.root_controller)


if __name__ == "__main__":
    root = Tk()
    obj = Controlador(root)
    root.mainloop()
        