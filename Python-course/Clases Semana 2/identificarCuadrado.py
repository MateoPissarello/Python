# pedirle al usuario el ancho y el alto de un rectangulo y decirle si es cuadrado

ancho = float(input("Por favor ingrese el ancho del rectángulo: "))
alto = float(input("Por favor ingrese el alto del rectángulo: "))

if ancho == alto:
    print("El rectángulo es cuadrado")
else:
    print("El rectángulo no es cuadrado")