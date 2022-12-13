# Librerias Utilizadas
from tkinter import *

# Clase Aplication para añadir componentes a la ventana
class Aplication:

    # Funcion Contructora de la Clase
    def __init__(self, window: Tk):
        self.win = window

        self.panel = PanedWindow(background = 'black')
        self.panel.place(x = 0, y = 0, width = 500, height = 500)

        self.menu = LabelFrame(self.panel, text = 'Menu')
        self.menu.place(x = 200, y = 200, width = 50, height = 50)




if __name__ == '__main__':

    window = Tk()  # Asignamos La Ventana

    # Damos un Ancho a la ventana
    windowWidth = 500

    # Damos un Alto a la ventana
    windowHeight = 500

    # Obtenemos el ancho de la pantalla y lo dividimos en 2 luego le restamos el ancho de la ventana dividido por 2
    xWindow = window.winfo_screenwidth() // 2 - windowWidth // 2

    # Obtenemos el alto de la pantalla y lo dividimos en 2 luego le restamos el alto de la ventana dividido por 2
    yWindow = window.winfo_screenheight() // 2 - windowHeight // 2

    # luego en esta variable juntamos todas la variables anteriores (500x500+1215+675)
    windowPosition = str(windowWidth) + "x" + str(windowHeight) + \
        "+" + str(xWindow) + "+" + str(yWindow)

    # damos el tamaño a la ventana con el metodo geometry, las validaciones anteriores son para que la ventana 
    # quede en la mitad de la pantalla
    window.geometry(windowPosition)

    # Añadimos un titulo
    window.title('Todos Somos Lindos (TSL)')

    # luego a la clase Aplication le enviamos la ventana
    Aplication(window)

    # Ejecutamos la ventana
    window.mainloop()
