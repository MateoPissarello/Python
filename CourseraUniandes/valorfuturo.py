capital = float(input("Ingrese el capital inicial: "))
tasa = float(input("Ingrese la tasa anual: "))
tiempo = int(input("Ingrese el número de años: "))

valor_futuro = capital * (1+(tasa/100)) ** tiempo

print(f"El valor futuro del monto inicial es de ${valor_futuro} trascurridos {tiempo} años y a una tasa del {tasa}% anual")