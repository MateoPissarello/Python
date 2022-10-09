#imprimir un texto simple
print("Buenos días")

#imprimir varios textos separados por espacios
print("texto1", "texto2")

#concadenar texto
primerTexto = "hola"
segundoTexto = "mundo"
holaMundo = primerTexto + " " + segundoTexto
print(holaMundo)

#formato textos con variables
miEdad = 10
print(f"Yo tengo {miEdad} años")

#nombramiento de variables

VariablePascalCase = "soy una variable con todas las iniciales mayusculas" #PascalCase
variableCamelCase = "primera palabra todo minuscula y las siguientes palabras con inicial mayuscula" #camelCase
variable_snake_case = "soy una variable que divide las palabaras con un _" #snake_case

#Operaciones aritméticas

Edad1 = 10
Edad2 = 40
#Operación de resta
diferenciaDeEdad = Edad2 - Edad1
#Operación de suma
sumaDeEdades = Edad2 + Edad1

#Operaciones de multiplicación y división
variable1 = 10
variable2 = 15.5
multiplicacion = variable1 * variable2
division = variable1 / variable2 #cuidado de no dividir por 0 porque sale un error

#jerarquía de las operaciones: potenciación > multiplicación y division > sumas y restas

variable1 = 10
variable2 = 50
variable3 = 20.7
variable4 = -10.1

#primero sumar v1 y v2, despues restar v3 y v4 y dividir esos dos resultados
resultado = (variable1 + variable2) / (variable3 - variable4)

#comando de input general de tipo texto
inputDeUsuario = input("por favor ingrese un valor: ")

#comando de input de tipo numerico
inputNumerico = int(input("por favor ingrese un valor numerico: "))
print(inputNumerico)