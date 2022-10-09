#paso 1: pedirle al usuario la cantidad de personas a ingresar

#paso 2: en un for de 0 a N pedir las edades de esas n personas

#paso 3: guardar las edades de esas personas en una lista

#paso 4: calcular el promedio de esas edades

numberofPersons = int(input("Por favor ingrese la cantidad de personas: "))
listOfAges = []

for i in range (0,numberofPersons):
    listOfAges.append(int(input(f"Por favor ingrese la edad de la persona {i + 1}: ")))

print(listOfAges)

average = sum(listOfAges) / len(listOfAges)
print(f"El promedio de las edades es {average} años")