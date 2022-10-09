def picas_y_fijas(numero_secreto:int, intento:int) -> dict:
    diccionario = {}
    intento = str(intento)
    numero_secreto = str(numero_secreto)
    i = 0
    picas = 0
    fijas = 0
    for numero in intento:
        if numero in numero_secreto and numero != numero_secreto[i]:
            i +=1
            picas += 1
        elif numero in numero_secreto and numero == numero_secreto[i]:
            i +=1
            fijas += 1
        else:
            i +=1
    diccionario["PICAS"] = picas
    diccionario["FIJAS"] = fijas

    return diccionario

picas_y_fijas(1234, 1325)