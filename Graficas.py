import matplotlib.pyplot as graf

class Graficar:

    def __init__(self, nombre, grafica, titulo = "", titulox = "", tituloy = "", ejex = [], ejey = []):
        self.nombre = nombre
        self.grafica = grafica
        self.titulo = titulo
        self.titulox = titulox
        self.tituloy = tituloy
        self.ejex = ejex
        self.ejey = ejey

    def Analizar(self):
        graf.bar(self.ejex, self.ejey) # ["producto 1", "producto 2", "producto 3"], [30,23,45]
        #Eje X
        graf.xlabel(self.titulox)

        #Eje y
        graf.ylabel(self.tituloy)

        #Titulo
        graf.title(self.titulo)
        graf.show()