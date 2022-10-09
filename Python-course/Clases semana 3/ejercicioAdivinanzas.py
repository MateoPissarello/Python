#Hacer un juego de adivinanzas
#el numero a adivinar es un aleatorio
#entre 0 y 20
#el codigo debe generar automaticamente el aleatorio
#el juego debe tener un maximo numero de intentos
#si me paso del maximo, pierdo

import random

def numberToFind(n):
    randint = random.randint(0,n)
    return randint


number = numberToFind(20)
print(number)

maxAttempts = 3
count = 0

while count < maxAttempts or find == number:
    find = int(input(f"Intenta adivinar el numero entre 0 y 20 tienes un máximo de {maxAttempts} intentos: "))
    count += 1
    if find == number:
        print("Felicidades has encontrado el numero")
    elif find != number:
        count += 1
        print(f"te quedan {maxAttempts - count} intentos")

