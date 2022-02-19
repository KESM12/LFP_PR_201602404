from turtle import color
import matplotlib.pyplot as graf
import numpy as np

class Graficar:

    def __init__(self, nombre, grafica, titulo = "", titulox = "", tituloy = "", ejex = [], ejey = []):
        self.nombre = nombre
        self.grafica = grafica
        self.titulo = titulo
        self.titulox = titulox
        self.tituloy = tituloy
        self.ejex = ejex
        self.ejey = ejey

    def Analizar(self, TipoGraf):
        print(TipoGraf)
        if TipoGraf == "barras" or TipoGraf == "barra":
            graf.bar(self.ejex, self.ejey) # ["producto 1", "producto 2", "producto 3"], [30,23,45]
            #Eje X
            graf.xlabel(self.titulox)
            #Eje y
            graf.ylabel(self.tituloy)
            #Titulo
            graf.title(self.titulo)
            graf.show()
        elif TipoGraf == "lineas" or TipoGraf == "linea":
            graf.plot(self.ejex, self.ejey, color='orange', linestyle='dashed', linewidth=3) 
            #Eje X
            graf.xlabel(self.titulox)
            #Eje y
            graf.ylabel(self.tituloy)
            #Titulo
            graf.title(self.titulo)
            graf.show()
        elif TipoGraf == "pie" or TipoGraf == "pastel":
            int_ejey = np.array(self.ejey)
            int_ejey = int_ejey.astype(int)
            graf.pie(int_ejey, labels=self.ejex) # [30,23,45], ["producto 1", "producto 2", "producto 3"]
            #Titulo
            graf.title(self.titulo)
            graf.show()
        else:
            return False
        