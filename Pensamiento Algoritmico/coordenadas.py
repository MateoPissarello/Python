CoordenadaX = int(input("Digite su coordenada X: "))

CoordenadaY =  int(input("Digite su coordenada Y: "))

CoordenadasTotales =  CoordenadaX , CoordenadaY

if (CoordenadaX == 0) or (CoordenadaY == 0):
    print("Su coordenada es neutra")

if CoordenadasTotales == 1:
    print("su coordenada pertence al cuadrante 1")



if  CoordenadaX > 1:
    if CoordenadaY > 1:
        print("su coordenada pertence al cuadrante 1 ")

if  CoordenadaX < 1 and CoordenadaX != 0:
    if CoordenadaY > 1:
        print("su coordenada pertence al cuadrante 2 ")

if CoordenadaX < 1 and CoordenadaX != 0:
    if CoordenadaY < 1 and CoordenadaY != 0:
        print("su coordenada pertence al cuadrante 3 ")



if CoordenadaX > 1:
    if CoordenadaY < 1 and CoordenadaY != 0:
        print("su coordenada pertence al cuadrante 4 ")

pregunta = input("Conocer el valor en la recta: ")
pregunta = pregunta.lower()
print(pregunta)

