
precioCompra = float(input("Por favor ingrese el precio total de su compra: "))

if precioCompra > 100000:
    descuento = precioCompra * 0.10
    print(f"Tiene un descuento de ${descuento} pesos")

else:
    descuento = 0
    print("Lamentamos informarle que no obtuvo descuento")

precioCompra = precioCompra - descuento
print(f"El valor a pagar es de ${precioCompra} pesos")