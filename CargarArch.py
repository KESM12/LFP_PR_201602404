from tkinter import Tk 
from tkinter.filedialog import askopenfilename

class CargarArchi():
   
    def __init__(self):
       self.texto = ""
       self.data = ""
       self.coddata = ""
       self.inst = ""
       self.codinst = ""

    def Leer(self):
        Tk().withdraw()
        x = ""
        try: 
            filename =  askopenfilename(title='Selecciona un archivo', filetypes=[('Archivos', 
                                                '*.data'),('Todos los archivos', '*')])
            print(filename)
        except:
            print('Error, no se ha seleccionado ningun archivo')
            return
