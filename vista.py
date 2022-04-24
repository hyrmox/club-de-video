from cProfile import label
import string
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from modelo import*
from regex import *
from tkinter import PhotoImage



class Ventana:
    def __init__(self, windows):
        self.root = windows 
        self.root.title("Video Club Los Ñires")
        self.root.geometry("600x250")
        self.root.config(bg="orange")
        self.root.resizable(0,0)

        direc = os.path.dirname(__file__)
        logo = os.path.join(direc, 'blue.png' )
        self.root.iconphoto(True, PhotoImage(file=logo))
        


        self.f = Frame(self.root)
        self.tree = ttk.Treeview(self.f)
        self.obj_base = Abmc ()
        self.valida = Validar()

        self.nombre = StringVar()
        self.apellido = StringVar()
        self.dni = StringVar()
        self.telefono = StringVar()
        self.pelicula = StringVar()
        self.alquiler = StringVar()

        self.titulo = Label(
                self.root,
                text="AGENDA DE PELICULAS 2022\n 1.0 2021 - Fernando Agustin Villoldo",
                fg="orange", bg="black",
                height=2, width=90, anchor=CENTER,
                relief="solid")
        self.titulo.place(x=0,y=0)


        #LABELS/ENTRYS

        self.nom = Label(self.root, text="Nombre: ", fg="orange", bg="black", relief="solid")
        self.nom.place(x=0, y=50)
        self.apel =  Label(self.root, text="Apellido: ", fg="orange", bg="black", relief="solid")
        self.apel.place(x=0, y=75)
        self.documento =  Label(self.root, text="DNI: ", fg="orange", bg="black", relief="solid")
        self.documento.place(x=0, y=100)
        self.telef = Label(self.root, text="Telefono: ", fg="orange", bg="black", relief="solid")
        self.telef.place(x=0, y=125)
        self.peli =  Label(self.root, text="Pelicula: ", fg="orange", bg="black", relief="solid")
        self.peli.place(x=0, y=150) 
        self.alqui = Label(self.root, text="Alquiler: ", fg="orange",bg="black")
        self.alqui.place(x=0, y=175)

        self.data_nom = Entry(self.root, width=16, textvariable=self.nombre)
        self.data_nom.place(x=60,y=50)
        self.data_apel = Entry(self.root, width=16, textvariable=self.apellido)
        self.data_apel.place(x=60,y=75)
        self.data_dni = Entry(self.root, width=16, textvariable=self.dni)
        self.data_dni.place(x=60,y=100)
        self.data_telef = Entry(self.root, width=16, textvariable=self.telefono)
        self.data_telef.place(x=60,y=125)
        self.data_peli = Entry(self.root, width=16, textvariable=self.pelicula)
        self.data_peli.place(x=60,y=150)
        self.data_alqui = Entry(self.root, width=16, textvariable=self.alquiler)
        self.data_alqui.place(x=60,y=175)

        #TREEVIEW
         
        self.f = Frame(self.root, bg="black",
                height=2, width=15, relief="solid")
        self.f.place(x=0,y=0)

        self.cont = Frame(self.root, bg="white", height=238, width=580,bd=5, relief="solid")
        self.cont.place(x=10, y=260)
        self.tree = ttk.Treeview(self.cont, columns=(
                "column1", "column2", "column3", "column4", "column5", "column6", "column7"), show="headings")
        
        self.tree.heading("#1", text="ID")
        self.tree.column("#1", minwidth=25, width=31, stretch=NO, anchor="c")
        self.tree.heading("#2", text="Nombre")
        self.tree.column("#2", minwidth=50, width=90, stretch=NO, anchor="c")
        self.tree.heading("#3", text="Apellido")
        self.tree.column("#3", minwidth=50, width=90, stretch=NO, anchor="c")
        self.tree.heading("#4", text="DNI")
        self.tree.column("#4", minwidth=50, width=90, stretch=NO, anchor="c")
        self.tree.heading("#5", text="Telefono")
        self.tree.column("#5", minwidth=50, width=89, stretch=NO, anchor="c")
        self.tree.heading("#6", text="Pelicula")
        self.tree.column("#6", minwidth=50, width=89, stretch=NO, anchor="c")
        self.tree.heading("#7", text="Alquiler")
        self.tree.column("#7", minwidth=50, width=89, stretch=NO, anchor="c")
        self.tree.place(x=0, y=0)
        
        #BOTONES

        self.button_guard = Button(self.root, text="Guardar\nContacto",
                                 fg="orange", bg="black", relief="solid",
                                 height=2, width=10, command=self.alta
                                 )
        self.button_guard.place(x=450, y=50)

        self.button_elim = Button(self.root, text="Eliminar\nContacto",
                                fg="orange", bg="black", relief="solid", command=self.borrar,
                                height=2, width=10
                                )
        self.button_elim.place(x=450,y=100)

        self.button_mod = Button(self.root, text="Modificar\nContacto",
                                fg="orange", bg="black", relief="solid"
                                , height=2, width=10, command=self.modi
                                )
        self.button_mod.place(x=450,y=150)

        self.button_mostrartree = Button(self.root, text="Desplegar\nTreeview",
                                    fg="orange", bg="black", relief="solid",
                                    height=2, width=10, command=self.mostrar)
        self.button_mostrartree.place(x=10, y=200)

        self.button_ocultartree = Button(self.root, text="Ocultar\nTreeview",
                                    fg="orange", bg="black", relief="solid",
                                    height=2, width=10, command=self.ocultar)
        self.button_ocultartree.place(x=10, y=520)

    def alta(self):
        if not self.valida.val_letras(self.nombre):
            return messagebox.showinfo(
                message="El campo debe contener solo letras de la A a la Z", 
                title="ERROR DE VALIDACION EN NOMBRE")
        if not self.valida.val_letras(self.apellido):
            return messagebox.showinfo(
                message="El campo debe contener solo letras de la A a la Z", 
                title="ERROR DE VALIDACION EN APELLIDO")
        if not self.valida.val_numeros(self.dni):
            return messagebox.showinfo(
                message="El campo solo permite carateres numericos", 
                title="ERROR DE VALIDACION DNI")
        if not self.valida.val_numeros(self.telefono):
            return messagebox.showinfo(
                message="El campo solo permite caracteres numericos", 
                title="ERROR DE VALIDACION TELEFONO")
        if not self.valida.val_letras(self.pelicula):
            return messagebox.showinfo(
                message="El campo debe contener solo letras de la A a la Z", 
                title="ERROR DE VALIDACION PELICULA")
        if not self.valida.val_letras(self.alquiler):
            return messagebox.showinfo(
                message="El campo debe contener solo letras de la A a la Z", 
                title="ERROR DE VALIDACION ALQUILER")
        
        else:
            self.obj_base.alta(self.nombre,
                            self.apellido, self.dni, self.telefono, self.pelicula, 
                            self.alquiler, self.tree)

    def borrar(self):
        self.obj_base.baja(self.tree)

    def modi(self):
        if not self.valida.val_letras(self.nombre):
            return messagebox.showinfo(
                message="El campo debe contener solo letras de la A a la Z", 
                title="ERROR VALIDACION NOMBRE")
        if not self.valida.val_letras(self.apellido):
            return messagebox.showinfo(
                message="El campo debe contener solo letras de la A a la Z", 
                title="ERROR VALIDACION APELLIDO")
        if not self.valida.val_numeros(self.dni):
            return messagebox.showinfo(
                message="El campo debe contener solo letras de la A a la Z", 
                title="ERROR VALIDACION DNI")
        if not self.valida.val_numeros(self.telefono):
            return messagebox.showinfo(
                message="El campo debe contener solo letras de la A a la Z", 
                title="ERROR VALIDACION TELFONO")
        if not self.valida.val_peli(self.pelicula):
            return messagebox.showinfo(
                message="El campo debe contener letras de la A a la Z y numeros de 0 al 9", 
                title="ERROR VALIDACION PELICULA")
        if not self.valida.val_letras(self.alquiler):
            return messagebox.showinfo(
                message="El campo debe contener solo letras de la A a la Z", 
                title="ERROR VALIDACION ALQUILER")
        else:
            self.obj_base.modificar(self.nombre, self.apellido,
                                    self.dni, self.telefono, self.pelicula, self.alquiler, self.tree)
    


    def actualizar(self):
        self.obj_base.actualizar_treeview(self.tree)

    def ocultar(self):
        self.root.geometry("600x250")

    def mostrar(self):
        self.root.geometry ('600x570')  

