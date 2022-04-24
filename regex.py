import re
from tkinter import E

class Validar():
    def __init__(self):
        pass

    def val_letras(self, val_letras):
        
        reg_letras = r"(^[A-Za-záéíóúñ\s]{1,}[\.]{0,1}[A-Za-z0-9\s]{0,}$)"
        return re.match(reg_letras, val_letras.get())

    def val_peli(self, val_peli):
        
        reg_pel = r"(^[A-Za-záéíóúñ\s]{1,}[\.]{0,1}[A-Za-z0-9\s]{0,}$)"
        return re.match(reg_pel, val_peli.get())

    def val_numeros(self, val_numeros):

        reg_numeros = r"(^([0-9])+$)"
        return re.match(reg_numeros, val_numeros.get())
    
    def val_todos(self, l1, n1, p1):
        return(self.val_letras(l1) and self.val_numeros(n1) and self.val_peli(p1))
