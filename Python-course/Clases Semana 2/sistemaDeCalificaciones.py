
notasDelEstudiante = float(input("Por favor introduzca su calificacion: "))

if notasDelEstudiante >= 0 and notasDelEstudiante <= 5:

    if notasDelEstudiante >= 0 and notasDelEstudiante < 3:
        print("insuficiente")
    elif notasDelEstudiante >= 3 and notasDelEstudiante < 4:
        print("Aceptable")
    elif notasDelEstudiante >= 4 and notasDelEstudiante < 4.6:
        print("Sobresaliente")
    else:
        print("Excelente")
else:
    print("La calificación insertada es inválida") 