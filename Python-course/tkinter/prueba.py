import tkinter

ventana = tkinter.Tk() #fundamental para crear la ventana
ventana.geometry("400x300") #sirve para darle tamaño a la ventana
#etiqueta = tkinter.Label(ventana, text = "Hola Mundo", bg = "blue") #Añadir un texto, pide 2 parametros, en que ventana se va a ubicar y el texto
#etiqueta.pack(fill = tkinter.BOTH, expand = True) #Para que se muestre nuestro texto 
def saludo(nombre):
    print("Hola " + nombre)

boton1 = tkinter.Button(ventana, text = "Sí", padx = 40, pady = 50, command = lambda: saludo("Manolo"))
boton1.pack()
ventana.mainloop() #fundamental para crear la ventana