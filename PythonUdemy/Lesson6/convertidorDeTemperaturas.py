def celciusAFahrenheit(celcius):
    return (celcius * 9/5) + 32
def fahrenheitACelcius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celcius = float(input("Inserte una temperatura para convertirla a grados fahrenheit: "))
print(f"{celcius}° a fahrenheit son {celciusAFahrenheit(celcius):.2f}°") #Con el :.2f se pueden redondear decimales
fahrenheit = float(input("Inserte una temperatura para convertirla a grados celcius: "))
print(f"{fahrenheit}° a celcius son {fahrenheitACelcius(fahrenheit):.2f}°")