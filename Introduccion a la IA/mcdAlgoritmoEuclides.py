# Entrada de datos
numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Digite el segundo número: "))
#Identificar si alguno de los dos números es igual a 0
if numero1 == 0:
    mcd = numero2
    print(f"El maximo comun divisor es {mcd}")
elif numero2 == 0:
    mcd = numero1
    print(f"El maximo comun divisor es {mcd}")

else:    
    while (numero1 % numero2 != 0):
        residuo = numero1 % numero2
        numero1 = numero2
        numero2 = residuo
    print(f"El maximo comun divisor es {numero2}")




