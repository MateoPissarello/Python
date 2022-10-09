class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos
    def mostrar_detalle(self): #metodo de instancia
        print(f"Persona: {self.nombre}, {self.apellido}, {self.edad}, {self.valores}, {self.terminos}")
        
persona1 = Persona("Carla", "Fernandez", 18, "4128912312", 2, 3, 5, m = "manzana", p = "pera") #Con Persona() se llama al método __init__
persona2 = Persona("Estefanía", "Medina Rios", 17)
persona1.mostrar_detalle()
persona1.telefono = "3103291381" #Esta es una forma de añadir un atributo a un objeto, pero los demas objetos creados no lo compartiran
#Persona.mostrar_detalle(persona1)
persona2.mostrar_detalle()