from fileinput import filename
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.tix import Tree

class CargarArch():

    def __init__(self):
        self.texto = ""
        self.coddata = 1 #id_data
        self.codinst = 1
        self.data = {}
        self.inst = {}
    
    def Leer(self, ext):
        arch_da = "" #x
        arch_ins = ""
        Tk().withdraw()
        try:
            filename = askopenfilename(title='Selecciona un archivo',
                                            filetypes=[('Archivos', f'*{ext}'), # -> concatena -> *.data o *.lfp
                                                        ('All Files', '*')])
            # print(filename)
            with open(filename, encoding='utf-8') as infile:
                arch_da = infile.read().strip()
            # print(str(arch_da))
        except:
            print('Error, no se ha seleccionado ningun archivo')
            return
        
        #arch_da = arch_da.upper() # -> MAYUSCULAS
        arch_da = arch_da.lower() # -> minusculas

        com = False
        for letra in arch_da:
            if letra != '\"':
                if (letra != " " and letra != "\n" and letra != "\t") or com:
                    arch_ins += letra
            elif not com:
                arch_ins += letra
                com = True
            else:
                arch_ins += letra
                com = False
        # print(arch_ins)
        self.texto = arch_ins
    
    def AnalizadorData(self):
        infor = self.texto #cade -->info
        mes = False #nombre --> mes
        anio = False
        par = 0
        datos = False

        mes_n = "" #mes_n
        anio_n = ""
        data = ""
        data_list = []

        cori = False
        cord = False
        caso = 0
        error = False

        for letra in infor:
            if mes == False:
                if letra != ':':
                    mes_n += letra
                else:
                    mes = True
            elif anio == False:
                if letra != "=":
                    anio_n += letra
                else:
                    anio = True
            elif letra == '(' and mes == True and anio == True:
                par += 1
            
            elif letra == ')' and mes == True and anio == True and par == True:
                par += 1
                print("Archivo leido correctamente")
                break
            elif datos == False:
                if letra == '[':
                    cori = True
                elif letra == ']' and cori == True:
                    cord = True
                elif cori == True and cord == False:
                    if letra == "\"":
                        caso += 1
                    else:
                        data += letra
                elif letra == ";":
                    if cori == True and cord == True and caso == 2:
                        lista = data.split(',')
                        if len(lista) != 3:
                            error = True
                            print("Error, no se puede leer este archivo")
                            break
                        try:
                            lista[1] = float(lista[1])
                            lista[2] = float(lista[2])
                        except:
                            error = True
                            print("Error, no se puede leer este archivo")
                            break
                        data_list.append(lista)
                        # print(lista)
                        data = ""
                        cori = False
                        cord = False
                        caso = 0
            else:
                error = True
                print("Error, no se puede leer este archivo")
                break
        
        if not error:
            anio_n = int(anio_n)
            if anio_n != 0 and mes_n != "" and data_list != [] and par == 2:
                self.data[self.coddata] = {'anio': anio_n, 'mes': mes_n, 'productos': data_list}
                self.coddata += 1 
            else:
                print("Error, no se puede leer este archivo")
            print(self.data) #imprime la mamada que ingreso del archivo data
    
    def AnalizadorInst(self):
        txt_inst = self.texto #txt_inst <-- cadena
        ini = txt_inst[0:2]
        a = len(txt_inst) - 3 # El tamanio de la lista (numero de datos)
        b = len(txt_inst)
        fin = txt_inst[a:b]

        caso = 0
        entry = False
        
        aux = {}
        if ini == "<¿" and fin == '"?>':
            txt_inst = txt_inst[2:]
            txt_inst = txt_inst[:-2]
            txt_inst += "$"
            comando = ""
            nombre = ""

            for letra in txt_inst:
                if letra != ":" and caso == 0:
                    comando += letra
                elif letra == ":":
                    caso = 1
                elif letra == '"':
                    if entry:
                        entry = False
                    else:
                        entry = True
                elif entry == True:
                    nombre += letra
                elif (letra == "," and caso == 1) or letra == "$":
                    if comando == 'nombre':
                        aux[comando] = nombre  # {'nombre': "cambio1"}
                    elif comando == 'grafica':
                        aux[comando] = nombre
                    elif comando == 'titulo':
                        aux[comando] = nombre
                    elif comando == 'titulox':
                        aux[comando] = nombre
                    elif comando == 'tituloy':
                        aux[comando] = nombre
                    else:
                        print("Error, no se reconoce este comando")
                        aux = {}
                        break
                    nombre = ""
                    comando = ""
                    caso = 0
                else:
                    print("Error, no se puede leer este archivo")
                    aux = {}
                    break
            
            if 'nombre' in aux and 'grafica' in aux:
                self.inst[self.codinst] = aux
                self.codinst += 1
                print(self.inst)
            else:
                print("Error, no se puede almacenar esta informacion, faltan datos")                    

        else:
            print("Error, no se puede leer este archivo")

    def EjeX(self, id):
        ejex = []
        if id in self.data:
            for p in self.data[id]['productos']:
                ejex.append(p[0])
        return ejex
    
    def EjeY(self, id):
        ejey = []
        if id in self.data:
            for p in self.data[id]['productos']:
                ejey.append(p[2])
        return ejey

    def getData(self):
        for dato in self.data:
            print(str(dato)+".", self.data[dato]['mes'])
        res = input('Seleccione una de las opciones: \n')
        return int(res)
    
    def getinst(self, id):
        if id in self.inst:
            return self.inst[id]