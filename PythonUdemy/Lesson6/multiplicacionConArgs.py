def multiplicar(*args):
    resultado = 1
    for i in args:
        resultado *= i
    return resultado

print(multiplicar(3,5,15,3))