
def mismos_digitos(a:int, b:int):
    mismosDigitos = False
    maximo = max(a,b)
    maximo = str(maximo)
    minimo = min(a,b)
    minimo = str(minimo)
    for numero in maximo:
        if numero in minimo :
            mismosDigitos = True
        else:
            mismosDigitos = False
    for numero in minimo:
        if numero in maximo:
            mismosDigitos = True
        else:
            mismosDigitos = False
    return print(mismosDigitos)

mismos_digitos(111234,12345)
        
