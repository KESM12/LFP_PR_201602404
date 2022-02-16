import CargarArch as CargarArchi
a = CargarArchi


class Menu:
    def Menu():
        while (True):
            print("--------Menu--------\n" +
            "1.- Cargar Data\n"+ 
            "2.- Cargar instrucciones\n"+ 
            "3.- Cargar Data\n"+
            "4.- Analizar\n"+ 
            "5.- Reportes\n"+
            "6.- Salir")
            num = input("Elija la opción: \n")
            if num == "1":
               a.CargarArchi()
            elif num == "2":
               pass
            elif num == "3":
                pass
            elif num == "4":
                pass
            elif num == "5":
                pass
            elif num == "6":
                break