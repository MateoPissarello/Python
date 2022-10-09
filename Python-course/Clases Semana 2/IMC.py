#Paso 1: pedirle al usuario su peso en Kg
peso = float(input("Por favor ingrese su peso en Kg: "))
#Paso 2: pedirle al usuario su estatura en cm
estatura = float(input("Por favor ingrese su estatura en m: "))
#Paso 3: Aplicar la formula del IMC
imc = peso / (estatura ** 2)
#Paso 4: Mostrar IMC dependiendo del caso

if imc < 18.5:
    print("Usted tiene una condición de peso inferior al normal")
elif imc >= 18.5 and imc < 25:
    print("Usted tiene una condición de peso normal")
elif imc >= 25 and imc < 30:
    print("Usted tiene sobrepeso")
else:
    print("Usted tiene obesidad")

print(f"Su índice de masa corporal es de {imc} kg/m2")


   

