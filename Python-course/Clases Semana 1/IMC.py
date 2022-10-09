#Paso 1: pedirle al usuario su peso en Kg
peso = int(input("Por favor ingrese su peso en Kg: "))
#Paso 2: pedirle al usuario su estatura en cm
estatura = float(input("Por favor ingrese su estatura en m: "))
#Paso 3: Aplicar la formula del IMC
imc = peso / (estatura** 2)
#Paso 4: Mostrar IMC dependiendo del caso

if imc >= 25:
    print(f"Ojo, tienes sobrepeso.\n Tu IMC es de {imc} kg/m2")
else:
    print(f"No tienes sobrepeso.\n Tu IMC es de {imc} kg/m2")
   


