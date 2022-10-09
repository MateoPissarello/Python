import math as mt

def logaritmoNatural(x,n):
    repeticiones = n+1
    i = 0
    resultado = 0
    while True:
        if x <= 0:
            resultado = print("No se puede realizar esta operacion para numeros menores o iguales a 0")
        if i < repeticiones:
            resultado += (1/((2*i)+1))*(((x**2)-1)/((x**2)-1))**((2 * i)+1)
            i+= 1
        else:
            return resultado
        
print(logaritmoNatural(0.1,69))