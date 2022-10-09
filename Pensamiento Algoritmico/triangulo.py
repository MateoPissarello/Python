import math as mt
def orientacionTriangulo(p1,p2,p3):
    return ((p2[0] - p1[0])*(p3[1] - p1[1]))-((p2[1] - p1[1])*(p3[0] - p1[0])) > 0
def puntoDentroDelTriangulo(p1,p2,p3,p):
    orientacion1 = orientacionTriangulo(p,p1,p2)
    orientacion2 = orientacionTriangulo(p,p2,p3)
    orientacion3 = orientacionTriangulo(p,p3,p1)
    if orientacion1 and orientacion2 and orientacion3:
        verdaderoOFalso = True
    else:
        verdaderoOFalso = False
    return verdaderoOFalso
        
#Reconocer puntos del triangulo
medidaLadoTriangulo = int(input("Ingrese la medida de los lados de su triangulo equilatero: "))
#Punto ingresado
coordenadaX = float(input("Ingrese la coordenada en x de su punto: "))
coordenadaY = float(input("Ingrese la coordenada en y de su punto: "))
puntoIngresado = (coordenadaX, coordenadaY)
#Puntos triangulo
puntoA = (0,0)
#Calular la altura del triangulo con el teorema de pitagoras
catetoAdyacente = medidaLadoTriangulo/2
hipotenusa = medidaLadoTriangulo
altura = mt.sqrt((hipotenusa)**2 - (catetoAdyacente)**2)
print(altura)
# redondeamos el valor obtenido
altura = round(altura,1)
print(altura)
puntoB = (catetoAdyacente,altura)
puntoC= (0,medidaLadoTriangulo) 
#Calcular
print(puntoDentroDelTriangulo(puntoA,puntoB,puntoC,puntoIngresado))
#Verificar si el punto esta dentro del triangulo usando vectores
#V1_AB = ((puntoB[0] - puntoA[0]), (puntoB[1] - puntoA[1])) # (x2 - x1, y2 - y1)
#V2_AC = ((puntoC[0] - puntoA[0]), (puntoC[1] - puntoA[1])) # (x3 - x1, y3 - y1)
#Orientacion positiva



