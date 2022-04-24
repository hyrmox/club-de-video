import datetime
import os

def regist_log(funcion):
    def envoltura(*args, **kwargs):
        envoltura.nllamada += 1
        actual = datetime.datetime.now()
        ruta = os.path.dirname(os.path.abspath(__file__)) + "\\Registro.txt"
        log = open(ruta, "a")
        linea = ("Evento: "+funcion.__name__,"Contador de registros: "+ str(envoltura.nllamada),
                "Nombre: "+args[1].get(), "Apellido: "+args[2].get(),
                "DNI: "+args[3].get(), "Telefono: "+args[4].get(), "Pelicula: "+args[5].get(),
                "Alquiler: "+args[6].get(),"fecha: "+ str(actual))
        slinea = str(linea)            
        log.write(slinea+"\n***************************\n")
        log.close()
        return funcion(*args, **kwargs)
    envoltura.nllamada = 0
    return envoltura
    
def regist_log2(funcion):
    def envoltura(*args, **kwargs):
        envoltura.nllamada += 1
        actual = datetime.datetime.now()
        ruta = os.path.dirname(os.path.abspath(__file__)) + "\\Registro.txt"
        log = open(ruta, "a")
        linea = ("Evento: "+funcion.__name__,"Contador de registros: "+ str(envoltura.nllamada), "fecha: "+ str(actual))
        slinea = str(linea)            
        log.write(slinea+"\n***************************\n")
        log.close()
        return funcion(*args, **kwargs)
    envoltura.nllamada = 0
    return envoltura


