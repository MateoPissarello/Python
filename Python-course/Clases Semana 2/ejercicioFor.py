
listOfNumbers = [-10, 50, 800, 9, 6, 23.5]
print(len(listOfNumbers))

print(sum(listOfNumbers))

count = 0
for number in listOfNumbers:
    count += 1
print("El total de elementos en la lista es", count)

suma = 0
for number in listOfNumbers:
    suma = suma + number
print("La suma de los elementos en la lista es ", suma)

print("El promedio de los datos es", suma / count)