#Paso 1: pedirle al usuario el valor total de la factura
totalFactura = int(input("¿Cual es el total de la factura?: "))

#Paso 2: pedirle al usuario el valot que quiere dar de propina
valorPropina = int(input("Por favor ingrese el valor que quiere dar de propina: "))

#Paso 3: Hacer el calculo de la propina
propina = totalFactura * valorPropina / 100

#Paso 4: Mostrarle al usuario el valor de la propina
print(f"El valor de propina es: ${propina} pesos")
