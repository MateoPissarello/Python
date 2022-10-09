def ordenar_cadena(cadena:str):
    cadenaOrdenada = sorted(cadena)
    cadenaVacia = ""
    for letra in cadenaOrdenada:
        cadenaVacia += letra
    return cadenaVacia

ordenar_cadena("klñ")