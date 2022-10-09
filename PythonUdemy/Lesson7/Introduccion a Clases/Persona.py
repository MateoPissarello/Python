
class Persona:
    def __init__(self, nombre, apellido, edad):  #parecido a un constructor en python
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
persona1 = Persona("Carla", "Fernandez", 18) #Con Persona() se llama al método __init__
print(f"Objeto persona uno:\nNombre: {persona1.nombre}\nApellido: {persona1.apellido}\nEdad: {persona1.edad}")
print("-"*20)
persona2 = Persona("Yuliana", "Peña", 16)
print(f"Objeto persona dos:\nNombre: {persona2.nombre}\nApellido: {persona2.apellido}\nEdad: {persona2.edad}")

#Modificar los valores de un objeto una vez creado (no recomendable, despues se hara con metodos mediante encapsulamiento)
print("-"*20)
persona1.nombre = "Estefania"
persona1.apellido = "Medina Rios"
persona2.edad = 17
print(f"Objeto persona uno:\nNombre: {persona1.nombre}\nApellido: {persona1.apellido}\nEdad: {persona1.edad}")