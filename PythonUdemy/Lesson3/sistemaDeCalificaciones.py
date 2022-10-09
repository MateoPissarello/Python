calificacion = int(input("Proporciona una calificación entre 0 y 10: "))
letraDeCalificacion = None

if calificacion >= 9 and calificacion <= 10:
    letraDeCalificacion = "A"
elif calificacion >= 8 and calificacion < 9:
    letraDeCalificacion = "B"
elif calificacion >= 7 and calificacion < 8:
    letraDeCalificacion = "C"
elif calificacion >= 6 and calificacion < 7:
    letraDeCalificacion = "D"
elif calificacion >= 0 and calificacion < 6:
    letraDeCalificacion = "F"
else:
    letraDeCalificacion = "Valor desconocido"

print(letraDeCalificacion)