class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre #Poniendo una linea antes del nombre logramos privatizar el atributo (encapsularlo) (Esto es para indicarnos a nosotros mismos, en python aun asi se puede modificar, excepto si colocamos __) 
        self._apellido = apellido
        self._edad = edad
    @property  #Este decorador sirve para indicar que este metodo va a recuperar el nombre de self._nombre, asi que lo va a encapsular
    def nombre(self):
        return self._nombre
    #Si comentamos el setter ahora sera un atributo solo de lectura "read-only"
    @nombre.setter #Decorador para el setter, para llamarlo como si fuese un atributo de la clase
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self,edad):
        self._edad = edad
    def mostrar_detalle(self): #metodo de instancia
        print(f"Persona: {self._nombre}, {self._apellido}, {self._edad}")
    def __del__(self): #destructor de objetos
        print(f"Persona: {self._nombre} {self._apellido}")
if __name__ == "__main__":
    persona1 = Persona("Carla", "Fernandez", 18) #Con Persona() se llama al método __init__
    #persona1._nombre = "Juan Carlos" #Esto no deberiamos hacerlo
    persona1.nombre = "Mateo"
    persona1.apellido = "Pissarello"
    persona1.edad = 17
    print(persona1.nombre)
    persona1.mostrar_detalle()
    print(persona1.nombre) #No hay que colocar parentesis
    print("1",__name__)#nombre del modulo