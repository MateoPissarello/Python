ventas = float(input("Por favor ingrese el valor total de las ventas: "))

if ventas < 5000000:
    comision = (2.5 * ventas) / 100

elif ventas >= 5000000 and ventas < 15000000:
    comision = (7.5 * ventas) / 100

elif ventas >= 15000000 and ventas < 30000000:
    comision = (11.5 * ventas) / 100

elif ventas >= 30000000 and ventas < 55000000:
    comision = (15 * ventas) / 100

else:
    ventas = ventas - 55000000
    comision = (7.5 * ventas) / 100 + 3050000

print(f"Su comision corresponde a ${comision} pesos")

