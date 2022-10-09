#Imprimir algo no quiere decir que se retorne algo.
from unittest import result


def sumar (a:int,b:int):
    return a + b

resultado = sumar(5, 3)

print(f"Resultado de la suma: {resultado}")
#print(f"Resultado de la suma: {sumar(5, 3)}")