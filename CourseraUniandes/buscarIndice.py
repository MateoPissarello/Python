def buscar_elemento(entrada:list, buscado:int):
    if buscado in entrada:
        indice = entrada.index(buscado)
    else:
        indice = -1
    return indice