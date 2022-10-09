from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from FiguraGeometrica import FiguraGeometrica

#figura = FiguraGeometrica() #Como es una clase abstracta no podemos crear objetos de esta clase(instanciar)
print("Creación objeto cuadrado".center(50,"*"))
cuadrado1 = Cuadrado(5,"rojo")
cuadrado1.set_alto = 9
cuadrado1.set_ancho = 9
print(f"El area del cuadrado es: {cuadrado1.calcular_area()}")
print(cuadrado1)
#MRO - Method Resolution Order 
print(Cuadrado.mro()) #El MRO cambia ya que es una clase abstracta

