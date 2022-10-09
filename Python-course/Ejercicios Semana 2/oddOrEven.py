listOfNumbers = [7, 2, 5, 10, 12, 9, 4, 8]


countOdd = 0
countEven = 0

for i in listOfNumbers:
    if i % 2 == 0:
        countEven += 1
    else:
        countOdd += 1
    
print("La cantidad de numeros pares es de", countEven)
print("La cantidad de numeros impares es de", countOdd)
    