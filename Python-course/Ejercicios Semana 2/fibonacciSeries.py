#Obtener la secuencia Fibonacci entre los numeros 0 al 50

# la suma de los dos numeros anteriores crea el siguiente numero de la secuencia: 0 1 (0+1) 1 (1+1) 

listFibonacci = [0, 1]

count = 1

while len(listFibonacci) < 50:
   listFibonacci.append(listFibonacci[count] + listFibonacci[count - 1])
   count += 1

print(listFibonacci)





    
