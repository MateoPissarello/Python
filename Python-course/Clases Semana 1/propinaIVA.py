#Total de la factura 
valorTotalFactura = int(input("¿Cual es el total de la factura?: "))
#Porcentaje de propina que se quiere dar
porcentajeDePropina =  int(input("Valor de la propina: "))
#Calcular IVA
valorIVA = (valorTotalFactura * 0.19)
#Calcular el subtotal (total de factura - valor del IVA)
subtotal = valorTotalFactura - valorIVA
#Calcular el valor de la propina (subtotal * propina / 100)
propina = (subtotal * porcentajeDePropina) / 100
#Mostrar el resultado
print(f"El valor total de la factura fue ${valorTotalFactura} pesos")
print(f"El valor del IVA fue ${valorIVA} pesos")
print(f"El valor del subtotal fue ${subtotal} pesos")
print(f"la propina es de ${propina} pesos")
print(f"El valor total de la compra mas la propina es ${valorTotalFactura + propina} pesos")
