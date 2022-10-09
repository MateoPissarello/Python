cantidadNumerosAIngresar = int(input("Ingrese la cantidad de numeros a ingresar: "))
listaNumeros = []
for i in range(0,cantidadNumerosAIngresar):
    numero = int(input(f"Digite el numero {i+1}: "))
    listaNumeros.append(numero)

suma = sum(listaNumeros)
print(f"La suma de los numeros ingresados es {suma}")