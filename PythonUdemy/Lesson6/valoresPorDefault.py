from numbers import Integral


def sumar(a:int = 0, b:int = 0) -> int:
    return a + b

resultado = sumar()
print(f"Resultado sumar: {resultado}")
print(f"Resultado sumar: {sumar(2,8)}")
