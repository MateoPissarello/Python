
def sucesion_fibonacci(cantidad_numero:int):
    a = 0
    b = 1
    lista = []
    if cantidad_numero == 1:
        lista.append(a)
    elif cantidad_numero == 2:
        lista.append(a)
        lista.append(b)
    else:
        lista.append(a)
        lista.append(b)
        while (cantidad_numero-2) > 0:
            suma = a + b
            lista.append(suma)
            cantidad_numero -= 1
            a = b
            b = suma
    nuevaCadena = ""
    for i in lista:
        nuevaCadena += str(i) + ","
    nuevaCadena = nuevaCadena.rstrip(",")
    return nuevaCadena



sucesion_fibonacci(9)

