import math as mt
def cosine(x, n):
    x = x % (2 * mt.pi)
    if x > mt.pi:
        x = abs(x - 2 * mt.pi)
    if x > mt.pi / 2:
        return -cosine(mt.pi - x, n)
    total = 0
    for i in range(0, n + 1):
        total += ((-1) ** i) * (x**(2*i) / mt.factorial(2*i))
    return total

print(cosine(0.785398,69))