numero = int(input("Ingrese un numero para calcular su factorial: "))
def factorial(numero):
    if numero < 0:
        print("No se puede calcular el factorial")
    elif numero == 1 or numero == 0:
        return 1
    else:
        return numero * factorial(numero-1)

print(f"El factorial de el numero {numero} es {factorial(numero)}")

