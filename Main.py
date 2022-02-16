class Menu:
    def Menu():
        # p = principal() invocamos las opciones 
        while (True):
            print("--------Menu--------\n" +
            "1.- Cargar Data\n"+ 
            "2.- Cargar instrucciones\n"+ 
            "3.- Cargar Data\n"+ )
            
            num = input("Elija la opción: \n")
            if num == "1":
                ruta = input("Nombre del archivo: ")
                p.CargarData(ruta)
            elif num == "2":
                ruta = input("Nombre del archivo: ")
                p.CargaIns(ruta)
            elif num == "3":
            elif num == "4":
            elif num == "5":