
def contar_caracteres_repetidos(cadena:str):
    repetidos = []
    lista = []
    i = 0
    for letra in cadena:
        if letra in lista:
            continue
        else:
            lista.append(letra)
            repetidos.append(cadena.count(letra))
    listaTemp = []
    for numero in repetidos:
        if numero > 1:
            listaTemp.append(numero)
    sumaRepetidos = sum(listaTemp)
    #repetidos = repetidos.rstrip("]")
    #repetidos = repetidos.lstrip("[")
    
    return print(sumaRepetidos)
    



#    for letra in cadena:
#        if letra in lista:
#            cantidad = cadena.count(letra)
#            if cantidad > 1:
#                repetidos +=  1
#            else:
#                repetidos += 1
#        else:
#            lista.append(letra)
#    return print(repetidos)

contar_caracteres_repetidos("manzana")

