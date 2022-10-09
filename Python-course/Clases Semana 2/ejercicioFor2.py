listOfGrades = [
    1,
    2.4,
    4.5,
    2.4,
    4.3,
    3.8,
    3.1,
    3,
    2.7,
    4.5,
    5,
    2.1,
    1.8,
    2.4,
    4.3
]

contInsuficiente = 0
contAceptable = 0
contSobresaliente = 0
sumaInsuficiente = 0
sumaAceptable = 0
sumaSobresaliente = 0

for grade in listOfGrades:
    if grade < 3:
        contInsuficiente += 1
        sumaInsuficiente = sumaInsuficiente + grade
    elif grade >= 3 and grade < 4:
        contAceptable += 1
        sumaAceptable = sumaAceptable + grade
    else:
        contSobresaliente += 1
        sumaSobresaliente = sumaSobresaliente + grade

print ("la suma de los insuficientes es", sumaInsuficiente)
print ("la suma de los Aceptables es", sumaAceptable)
print ("la suma de los Sobresalientes es", sumaSobresaliente)

print ("la cantidad de los insuficientes es", contInsuficiente)
print ("la cantidad de los Aceptables es", contAceptable)
print ("la cantidad de los Sobresalientes es", contSobresaliente)

print ("El promedio de los insuficientes es", sumaInsuficiente / contInsuficiente)
print ("El promedio de los Aceptables es", sumaAceptable / contAceptable)
print ("El promedio de los Sobresalientes es", sumaSobresaliente / contSobresaliente)

