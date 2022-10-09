print("Hola Mundo")
print("Hola Mundo", "Este es otro mensaje", "Este es el tercero")

#declaracion de variables para calcular la diferencia de edad entre dos personas
edad = 10
edad_mama = 40

print("La diferencia entre las edades es: ", edad_mama - edad, "años")

resultado = "La diferencia entre las edades es: " + str(edad_mama - edad) + " años"
#Ejeplo del uso del comando especial "f" en un string donde se requiere realizar operaciones aritmeticas
resultado2 = f"La diferencia entre las edades es: {edad_mama - edad} años"
print(resultado)
print(resultado2)


#paso 1: pedir la edad de la persona 1
edad1 = input("Por favor ingrese la edad de la primera persona: ")

#paso 2: pedir la edad de la persona numero 2
edad2 = input("Por favor ingrese la edad de la segunda persona: ")
#paso 3: calcular la diferencia de las edades
diferencia_de_edad = int(edad1) - int(edad2)
#paso 4: imprimir la diferencia en las edades
print(f"la diferencia en las edades es de {diferencia_de_edad} años")
