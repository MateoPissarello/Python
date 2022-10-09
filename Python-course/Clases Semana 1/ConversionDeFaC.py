#Paso 1: pedir los °F
valorFahrenheit = int(input("Por favor ingrese una temperatura en grados Fahrenheit: "))
#Paso 2: Conversion, Fahrenheit a Celsius
valorCentrigrados = (valorFahrenheit - 32) * 5 / 9
#Paso 3: Mostrar conversion
print(f"{valorFahrenheit}°F son {valorCentrigrados}°C")

