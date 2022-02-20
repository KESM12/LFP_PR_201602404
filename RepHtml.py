import webbrowser

class Html2:
    
    def __init__(self, producto = [], precUnit = [], cantVendi = []):
        self.producto = producto #Producto self.ejex
        self.precUnit = precUnit #Precio Unitario
        self.cantVendi = cantVendi #Cantidad vendida

    def EscHtml(self):
        #print(self.producto)
        #Ganancia = precio * cantidad

        f = open('201602404.html','w')
        print('html')
        mensaje = """<html>
<head>
<title>Reportes</title>
</head>
<body>
Kevin Estuardo Secaida Molina 201602404

<h1>Reporte de productos</h1>
#aqui iria tabla con los productos ordenados de mayor a menor en funcion de las ganancias generadas 
(precio unitario *  cantidad vendida)

<h4>Producto menos vendido</h4>

<h4>Producto mas vendido</h4>
</body>

</html>"""
        #tablas

        f.write(mensaje)
        f.close()   
        webbrowser.open_new_tab('201602404.html')
