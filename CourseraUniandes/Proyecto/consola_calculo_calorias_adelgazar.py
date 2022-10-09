import calculadora_indices as clc

def inciar_aplicacion():
    peso = float(input("Ingrese el peso de la persona (en Kilogramos): "))
    altura = float(input("Ingrese la altura de la persona (en Centimetros): "))
    edad = int(input("Ingrese la edad de la persona (en años): "))
    valor_genero = float(input("Ingrese el valor 5 en caso de ser hombre y -161 en caso de ser mujer: "))
    print(clc.consumo_calorias_recomendado_para_adelgazar(peso,altura,edad,valor_genero))

inciar_aplicacion()   