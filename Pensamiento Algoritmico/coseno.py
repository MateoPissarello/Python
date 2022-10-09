import math as mt

def coseno (x,n):
    suma = 0
    i = 0
    while i < n + 1:
        suma += ((-1) ** i) * (x**(2*i)/mt.factorial(2*i))
        i+=1
    return suma

calculo = coseno(0.785398,69)
print('{:.20f}'.format(calculo))
