
class Persona:
    contador_personas = 0
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas
        
    def __init__(self, nombre, edad):
        self.id = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.id}, {self.nombre}, {self.edad}]'

persona1 = Persona("Marcos", "19")
print(persona1)
persona2 = Persona("Carla", "20")
print(persona2)
persona3 = Persona("Jose", "35")
print(persona3)
Persona.generar_siguiente_valor()
persona4 = Persona("Sofia", "15")
print(persona4)
print(f"Valor contador personas: {Persona.contador_personas}")
