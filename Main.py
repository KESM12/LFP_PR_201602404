from CargarArch import CargarArch
a = CargarArch


class Aplicacion:
    def __init__(self):
        self.Menu()

    def Menu(self):
        while (True):
            num = input("--------Menu--------\n" +
            "1.- Cargar Data\n"+ 
            "2.- Cargar instrucciones\n"+ 
            "3.- Cargar Data\n"+
            "4.- Analizar\n"+ 
            "5.- Reportes\n"+
            "6.- Salir\n"+
            "Seleccione una de las opciones\n")
            #num = input("Elija la opción: \n")
            if num == "1":
               a.Leer(self, '.data')
            #a.Analizar_1()
            elif num == "2":
               pass
            elif num == "3":
                pass
            elif num == "4":
                pass
            elif num == "5":
                pass
            elif num == "6":
                print('Adios.')
                break
            else:
                print('Ingrese una de las opciones por favor.')

b = Aplicacion()