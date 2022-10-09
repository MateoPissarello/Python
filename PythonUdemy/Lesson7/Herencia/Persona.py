class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self,edad):
        self._edad = edad
    def __str__(self):
        return f"Persona[Nombre: {self._nombre}, Edad: {self._edad}]" #Reescribimos el metodo __str___ que viene por defecto en la clase object el cual nos indica donde esta ubicado un objeto en la memoria por un string

class Empleado(Persona):  #El parentesis es la clase de la cual se va a heredar, con una coma se puede añadir mas de una
    def __init__(self, nombre,edad,sueldo):
        super().__init__(nombre,edad) #Metodo para obtener los atributos de la clase padre
        self._sueldo = sueldo
    @property
    def sueldo(self):
        return self._sueldo
    @sueldo.setter
    def sueldo(self,sueldo):
        self._sueldo = sueldo
    def __str__(self):
        return f"Empleado: [Sueldo: {self._sueldo}] {super().__str__()}"

if __name__ == "__main__":
    empleado1 = Empleado("Mateo", 17, "5000000")
    print(empleado1.nombre)
    print(empleado1.edad)
    print(empleado1.sueldo)