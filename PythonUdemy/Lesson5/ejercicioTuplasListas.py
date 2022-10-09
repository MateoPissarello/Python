#Dada la siguiente tupla crear una lista donde solo incluya los numeros menores a 5

tupla = (13, 1, 8, 3, 2, 5, 8)
listaMenorQue5 = []

for numero in tupla:
    if numero < 5:
        listaMenorQue5.append(numero)
    
print(listaMenorQue5)