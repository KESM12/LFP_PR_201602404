from CargarArch import CargarArch
a = CargarArch()


class Aplicacion:
    def __init__(self):
        self.Menu()

    def Menu(self):
        while (True):
            num = input("--------Menu--------\n" +
            "1.- Cargar Data\n"+ 
            "2.- Cargar instrucciones\n"+ 
            "3.- Analizar\n"+
            "4.- Reportes\n"+ 
            "5.- Salir\n"+
            "Seleccione una de las opciones\n")
            if num == "1":
               a.Leer('.data')
               a.AnalizadorData()
            elif num == "2":
               a.Leer('.lfp')
               a.AnalizadorInst()
            elif num == "3":
                pass
            elif num == "4":
                pass
            elif num == "5":
                print('Adios.')
                break
            else:
                print('Ingrese una de las opciones por favor.')

b = Aplicacion()