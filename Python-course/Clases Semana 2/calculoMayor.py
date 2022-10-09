#pedirle al usuario dos valores numericos. Imprimir el mayor de ellos

numero1 = float(input("Ingrese un valor numérico: "))
numero2 = float(input("Ingrese un segundo valor numérico: "))

if numero1 > numero2:
    print("El primer dato es mayor que el segundo")
elif numero2 > numero1:
    print("El segundo dato es mayor que el primero")
else:
    print("Los valores son iguales. No hay ninguno mayor que el otro")