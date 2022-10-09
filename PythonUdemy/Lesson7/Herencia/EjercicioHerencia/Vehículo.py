
class Vehiculo:
    def __init__(self,color,ruedas):
        self._color = color
        self._ruedas = ruedas
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,color):
        self._color = color
    def __str__(self):
        return f"Vehículo[Color: {self._color}, Ruedas: {self._ruedas}]"

class Coche(Vehiculo):
    def __init__(self, color, ruedas,velocidad):
        super().__init__(color, ruedas)
        self._velocidad = velocidad
    @property 
    def velocidad(self):
        return self._velocidad
    @velocidad.setter
    def velocidad(self,velocidad):
        self._velocidad  = velocidad
    def __str__(self):
        return f"Coche: Velocidad (km/h)[{self._velocidad}], {super().__str__()}"
    
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas,tipo):
        super().__init__(color, ruedas)
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self,tipo):
        self._tipo = tipo
    def __str__(self):
        return f"Bicicleta: Tipo[{self._tipo}], {super().__str__()}"


    