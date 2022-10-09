#imprmir la suma, la resta y la multiplicacion de dos numeros

def addTwoNumbers(n1, n2):
    suma = n1 + n2
    return suma

#Definir la funcion de resta

def subtractTwoNumbers(n1, n2):
    resta = n1 - n2
    return resta

#Definir la función de multiplicar

def multiplyTwoNumbers(n1, n2):
    return n1 * n2

#Funcion general para el cálculo
def calculateResult(n1,n2,operation): #operation: s, r, m
  
    if operation == "s":
        return addTwoNumbers(n1,n2)
    elif operation == "r":
        return subtractTwoNumbers(n1, n2)
    elif operation == "m":
        return  multiplyTwoNumbers(n1, n2)
    else:
        return  "error"
   


number1 = int(input("Por favor ingrese el primer número: "))
number2 = int(input("Por favor ingrese el segundo número: "))

suma = calculateResult(number1, number2, "s")
resta = calculateResult(number1, number2, "r")
multiplicacion = calculateResult(number1, number2, "m")

print("La suma es ", suma)
print("La resta es ", resta)
print("La multiplicacion es ", multiplicacion)
