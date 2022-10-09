def ocurrencias_caracter (cadena:str, caracter:str):
    ocurrencias = 0
    i = 0
    while(i < len(cadena)):
        if (cadena[i] == caracter):
            ocurrencias += 1
        i +=1
    return print(ocurrencias) #

ocurrencias_caracter("La Casa Blanca", "a")