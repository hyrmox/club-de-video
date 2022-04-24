from tkinter import*
from peewee import*
from decorador import*


db = SqliteDatabase('Clintes.db')

class Base(Model):
    class Meta:
        database = db


class Noticia(Base):
    id = AutoField()
    nombre = CharField()
    apellido = CharField()
    dni = IntegerField()
    telefono = IntegerField()
    pelicula = CharField()
    alquiler = CharField()

class Abmc:
    def __init__(self):
        
        try:
            db.connect()
            db.create_tables([Noticia])

        except:
            print("Error conexión")

    def actualizar_treeview(self, mitreeview):
        #limpieza de tabla
        records = mitreeview.get_children()
        for element in records:
            mitreeview.delete(element)
            
        query = Noticia.select()
        count=0
        for fila in query:
            if count %2==0:
                mitreeview.insert("", 'end', text=fila.id, values=(
                    fila, fila.nombre, fila.apellido, fila.dni, fila.telefono, fila.pelicula, fila.alquiler),tags=('impar',))
            else:
                mitreeview.insert("", 'end', text=fila.id, values=(
                    fila, fila.nombre, fila.apellido, fila.dni, fila.telefono, fila.pelicula, fila.alquiler),tags=('par',))
            count+=1
    @regist_log
    def alta(self, nombre, apellido, dni, telefono, pelicula, alquiler,  mitreeview):
               
        Noticia.insert({Noticia.nombre:nombre.get(), Noticia.apellido:apellido.get(),
            Noticia.dni:dni.get(), Noticia.telefono:telefono.get(), Noticia.pelicula:pelicula.get(),
                Noticia.alquiler:alquiler.get()}).execute()
        self.actualizar_treeview(mitreeview)
    @regist_log2
    def baja(self, mitreeview):
        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        datos = (valor_id["text"])

        Noticia.delete().where (Noticia.id==datos).execute()

        self.actualizar_treeview(mitreeview)
    @regist_log
    def modificar(self, nombre, apellido, dni, telefono, pelicula, alquiler, mitreeview):
        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        datos = (valor_id["text"])
        
        Noticia.update(nombre=nombre.get(), apellido=apellido.get(),
            dni=dni.get(), telefono=telefono.get(), pelicula=pelicula.get(), alquiler=alquiler.get()).where(Noticia.id == datos).execute()

        self.actualizar_treeview(mitreeview)
