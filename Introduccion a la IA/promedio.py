memoria = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
listaNumerosAñadidos = []
for i in range(1,6):
    numero = int(input("Digite el numero: "))
    listaNumerosAñadidos.append(numero)
    memoria[9+i] = numero

suma = sum(listaNumerosAñadidos)
promedio = suma / len(listaNumerosAñadidos)
memoria[15] = promedio

print(f"El promedio es {promedio}")
print(memoria)