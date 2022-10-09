def factorial(numero):
    if numero < 0:
        print("No se puede calcular el factorial")
    elif numero == 1 or numero == 0:
        return 1
    else:
        return numero * factorial(numero-1)

valor_n = int(input("Ingrese el valor de n: "))
valor_m = int(input("Ingrese el valor de m: "))
if valor_n < valor_m:
    print("No se puede hacer la combinatoria")
else:
    factorial_n = factorial(valor_n)
    factorial_m = factorial(valor_m)
    resta_nm = valor_n - valor_m
    factorial_nm = factorial(resta_nm)
    calcularCombinacion = factorial_n/(factorial_nm * factorial_m)

print(calcularCombinacion)