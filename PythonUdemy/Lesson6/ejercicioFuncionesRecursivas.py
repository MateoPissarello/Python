def imprimirNumeros(x):
    if x >= 1:
        print(x)
        return imprimirNumeros(x-1)
    elif x == 0:
        return
    elif x < 0:
        print(f"Valor incorrecto...")

imprimirNumeros(50)
