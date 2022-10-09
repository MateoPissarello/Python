def es_divisible(n:int,d:int):
    resultado = 0
    if n == 0 or d == 0:
        resultado = 0
    else:
        if n % (2 * d) == 0:
            resultado = 2
        elif n % d == 0:
            resultado = 1
        else:
            resultado = 0
    return resultado

print(es_divisible(10,0)) 


#print(10 // 0)