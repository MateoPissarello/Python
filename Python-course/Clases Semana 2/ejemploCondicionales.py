
numeroAEncontrar = 7

numeroIngresadoPorElUsuario = int(input("Adivina cuál número está registrado como variable: "))

if numeroIngresadoPorElUsuario > numeroAEncontrar:
    print("El numero que estas buscando es menor al que ingresaste")
elif numeroIngresadoPorElUsuario < numeroAEncontrar:
    print("El número que estás buscando es mayor al que ingresaste")
#elif numeroAEncontrar == numeroIngresadoPorElUsuario:
else:
    print("El número que ingresaste es el correcto")


