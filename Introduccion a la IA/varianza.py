memoria = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
listaNumerosAñadidos = []
numeroMenosPromedio = []
for i in range(1,6):
    numero = int(input("Digite el numero: "))
    listaNumerosAñadidos.append(numero)
    memoria[9+i] = numero

suma = sum(listaNumerosAñadidos)
promedio = suma / len(listaNumerosAñadidos)

for numero in listaNumerosAñadidos:
    operacion = (numero - promedio)**2
    numeroMenosPromedio.append(operacion)

varianza = sum(numeroMenosPromedio) / len(numeroMenosPromedio)
print(numeroMenosPromedio)
memoria[15] = varianza
print(memoria)


