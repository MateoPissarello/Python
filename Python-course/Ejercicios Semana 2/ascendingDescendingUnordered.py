
numbers = 4
listofNumbers = []

for number in range(0,numbers):
    listofNumbers.append(int(input(f"Por favor ingrese el primer numero {number + 1}: ")))
   
if listofNumbers[0] > listofNumbers[1] > listofNumbers[2] > listofNumbers[3]:
     print("Orden descendiente") 
elif listofNumbers[0] < listofNumbers[1] < listofNumbers[2] < listofNumbers[3]:
     print("Orden ascendente")
else:
     print("Desordenado")