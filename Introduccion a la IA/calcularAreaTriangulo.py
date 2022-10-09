import math as mt
primerLado = float(input("Ingrese la medida del primer lado en metros: "))
segundoLado = float(input("Ingrese la medida del segundo lado en metros: "))
angulo = float(input("Ingrese la medida del angulo que se forma: "))
gradosARadianes = (angulo * mt.pi)/180
calcularArea = round((((primerLado * segundoLado) * mt.sin(gradosARadianes))/2),2)

print(f"El area del triangulo es de {calcularArea}")
