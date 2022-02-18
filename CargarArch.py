from fileinput import filename
from tkinter import Tk
from tkinter.filedialog import askopenfilename
#from tkinter.ttk import Tree


class CargarArch():
   
    def __init__(self):
       self.texto = ""
       self.data = { }
       self.coddata = ""
       self.inst = { }
       self.codinst = ""

    def Leer(self, extension):
        x = ""
        y = ""
        Tk().withdraw()
        try:
            filename = askopenfilename(title='Selecciona un archivo',
                                            filetypes=[('Archivos', f'*{extension}'), 
                            # -> concatena -> *.data o *.lfp
                                                        ('All Files', '*')])
            #print(filename)
            with open(filename, encoding='utf-8') as infile:
                x = infile.read().strip()
            #print(str(x))
        except:
            print('Error, no se ha seleccionado ningun archivo')
            return
        
        #x = x.upper() # -> MAYUSCULAS
        x = x.lower() # -> minusculas

        com = False
        for letra in x:
            if letra != '\"':
                if (letra != " " and letra != "\n" and letra != "\t") or com:
                    y += letra
            elif not com:
                y += letra
                com = True
            else:
                y += letra
                com = False
        # print(y)
        self.texto = y