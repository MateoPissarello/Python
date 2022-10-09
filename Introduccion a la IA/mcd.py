from math import gcd
numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Digite el segundo número: "))
if numero1 == 0:
    mcd = numero2
elif numero2 == 0:
    mcd = numero1
else:
  mcd =  gcd(numero1,numero2)
print(f"El MCD es {mcd}")
