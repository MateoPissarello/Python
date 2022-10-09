from termcolor import colored
import math as mt
radio = 0
CoordenadaX = int(input(colored("Digite su coordenada X: ", "blue", attrs=['bold'])))
CoordenadaY =  int(input(colored("Digite su coordenada Y: ", "cyan", attrs=['bold'])))
CoordenadasTotales =  CoordenadaX , CoordenadaY

if (CoordenadaX == 0) or (CoordenadaY == 0):
    print(colored("\t\t Su coordenada es neutra\n", "cyan"))

if CoordenadasTotales == 1:
    print(colored("\t\t Su coordenada pertence al cuadrante 1\n", "red"))

if  CoordenadaX >= 1:
    if CoordenadaY >= 1:
        print(colored("\t\t Su coordenada pertence al cuadrante 1 \n", "green"))

if  CoordenadaX < 1 and CoordenadaX != 0:
    if CoordenadaY > 1:
        print("\t\t Su coordenada pertence al cuadrante 2\n ", "red")

if CoordenadaX < 1 and CoordenadaX != 0:
    if CoordenadaY < 1 and CoordenadaY != 0:
        print("\t\t Su coordenada pertence al cuadrante 3 \n")

if CoordenadaX > 1:
    if CoordenadaY < 1 and CoordenadaY != 0:
        print("\t\t Su coordenada pertence al cuadrante 4\n ")


print(colored("\t\t Desea conocer el valor con base a la recta\n ", "green"))
pregunta =str(input(""))
pregunta =pregunta.lower() # .lower sirve para convertir cualquier string a minuscula 

if pregunta == "si":
    if CoordenadaY == CoordenadaX:
        print(colored("\t\t Sus Coordenadas estan sobre la recta y=x \n", "yellow"))

    #por debajo de la recta 
    if CoordenadaX > 1 and CoordenadaY < 1 and CoordenadaY != 0:
        print("Sus Coordenadas estan debajo de la recta ")
    if 0 < CoordenadaY and 0 < CoordenadaX and CoordenadaY < CoordenadaX :
        print("Sus Coordenadas estan por debajo de la recta")
    if 0 > CoordenadaY and 0 > CoordenadaX and CoordenadaY < CoordenadaX :
        print("Sus Coordenadas estan por debajo de la recta")
    #por encima de la recta 
    
    if CoordenadaX < 1 and CoordenadaX != 0 and CoordenadaY > 1:
        print("Sus Coordenadas estan encima de la recta ")
    if 0 < CoordenadaY and 0 < CoordenadaX and CoordenadaY > CoordenadaX :
        print("Sus Coordenadas estan por encima de la recta")
    if 0 > CoordenadaY and 0 > CoordenadaX and CoordenadaY > CoordenadaX :
        print("Sus Coordenadas estan por encima de la recta")

print(colored("\t\t ¿Desea conocer si el valor esta dentro o fuera de la circunferencia ? \n", "red"))
pregunta =str(input(""))
pregunta=pregunta.lower() # .lower sirve para convertir cualquier string a minuscula 

if pregunta == "si":
    radio=int(input("\t\t Por favor digite el radio de la Circunferencia\n"))
    CalcularDistancia = mt.sqrt((CoordenadaX**2) + (CoordenadaY**2))
    if radio == CalcularDistancia:
        print("\t\t  Sus Coordenadas estan sobre la circunferencia\n ") 
    if radio < CalcularDistancia:
        print("\t\t Sus Coordenadas estan fuera de la circunferencia\n ")
    if radio > CalcularDistancia:
        print("\t\t Sus Coordenadas estan dentro de la circunferencia\n ")