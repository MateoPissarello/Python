import math as mt
def seno(x,n):
    suma = 0
    for i in range(n+1):
        suma += ((-1)** i/ mt.factorial(2*i+1)) * x**(2*i+1)
    return suma
calculo=(seno(0.0174533,45))
print('{:.20f}'.format(calculo))
