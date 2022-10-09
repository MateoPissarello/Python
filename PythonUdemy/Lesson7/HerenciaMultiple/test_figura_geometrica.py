from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print("Creación objeto cuadrado".center(50,"*"))
cuadrado1 = Cuadrado(5,"rojo")
cuadrado1.set_alto = 9
cuadrado1.set_ancho = 9
print(f"El area del cuadrado es: {cuadrado1.calcular_area()}")
print(cuadrado1)
print("Creación objeto rectángulo".center(50,"*"))
rectangulo1 = Rectangulo(5,8,"Azul")
print(rectangulo1)
print(f"El area del rectangulo es: {rectangulo1.calcular_area()}")
print("Creación objeto cuadrado2".center(50,"*"))
cuadrado2 = Cuadrado(6,"Aguamarina")
print(cuadrado2)
print(f"El area del cuadrado es: {cuadrado2.calcular_area()}")
print("Creación objeto rectángulo2".center(50,"*"))
rectangulo2 = Rectangulo(3,7, "Cobalto")
print(rectangulo2)
print(f"El area del rectangulo es de: {rectangulo2.calcular_area()}")
#MRO - Method Resolution Order 

