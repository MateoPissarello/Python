#pedirle al usuario los ingresos
ingresos = float(input("Por favor coloque sus ingresos: "))

#pedirle al usuario los costos
costos = float(input("Por favor ingrese los costos: "))

#calcular la ultilidad bruta (ingresos - costos)
utilidadBruta = ingresos - costos
print(f"La utilidad bruta de empresa es: ${utilidadBruta} pesos")

#pedirle al usuario los gastos
gastos = float(input("Por favor ingrese los gastos: "))

#calcular la utilidad operativa (utilidad bruta - gastos)
utilidadOperativa = utilidadBruta - gastos
print(f"La utilidad operativa de la empresa es: ${utilidadOperativa} pesos")

#calcular el impuesto a la renta (utilidad operativa * 0.3)
impuestoALaRenta = utilidadOperativa * 0.3
print(f"El impuesto a la renta de la empresa es: ${impuestoALaRenta} pesos")

#calcular la utilidad neta (utilidad bruta - impuesto a la renta)
utilidadNeta = utilidadOperativa - impuestoALaRenta
print(f"La utilidad neta de la empresa es: ${utilidadNeta} pesos")

