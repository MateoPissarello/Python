import calculadora_indices as clc

def inciar_aplicacion():
    peso = float(input("Ingrese el peso de la persona (en Kilogramos): "))
    altura = float(input("Ingrese la altura de la persona (en metros): "))
    edad = int(input("Ingrese la edad de la persona (en años): "))
    valor_genero = float(input("Ingrese el valor 10.8 en caso de ser hombre y 0 en caso de ser mujer: "))
    print(clc.calcular_porcentaje_grasa(peso,altura,edad,valor_genero))

inciar_aplicacion()   