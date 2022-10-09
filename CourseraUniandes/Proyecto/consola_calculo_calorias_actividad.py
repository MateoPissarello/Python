import calculadora_indices as clc

def inciar_aplicacion():
    peso = float(input("Ingrese el peso de la persona (en Kilogramos): "))
    altura = float(input("Ingrese la altura de la persona (en Centimetros): "))
    edad = int(input("Ingrese la edad de la persona (en años): "))
    valor_genero = float(input("Ingrese el valor 5 en caso de ser hombre y -161 en caso de ser mujer: "))
    valor_actividad = float(input("Si en la semana hace poca o ninguna actividad física, ingrese el valor 1.2, si realiza actividad física de 1 a 3 días a la semana, ingrese el valor 1.375, si realiza actividad física de 3 a 5 días a la semana, ingrese el valor 1.55, si realiza actividad física de 6 a 7 días a la semana, ingrese el valor 1.72, si realiza actividad física todos los días de la semana en la mañana y la tarde, ingrese el valor 1.9: "))
    print(clc.calcular_calorias_en_actividad(peso,altura,edad,valor_genero, valor_actividad))

inciar_aplicacion()   