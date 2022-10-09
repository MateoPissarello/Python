import calculadora_indices as clc

def inciar_aplicacion():
    peso = float(input("Ingrese el peso de la persona (en Kilogramos): "))
    altura = float(input("Ingrese la altura de la persona (en metros): "))
    print(clc.calcular_IMC(peso,altura))

inciar_aplicacion()   