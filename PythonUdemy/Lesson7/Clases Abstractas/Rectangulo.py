from FiguraGeometrica import FiguraGeometrica
from Color import Color
class Rectangulo(FiguraGeometrica,Color): #El orden en que se añaden las clases en herencia multiple es importante
    def __init__(self,ancho,alto,color):
       #super().__init__()
        FiguraGeometrica.__init__(self,ancho,alto) #Forma de añadir los atributos de clases padres en herencia multiple
        Color.__init__(self,color)

    def calcular_area(self):
        return self._alto * self._ancho
    def __str__(self):
        return f"{FiguraGeometrica.__str__(self)}, {Color.__str__(self)}"