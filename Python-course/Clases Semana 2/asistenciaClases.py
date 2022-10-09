
clases = int(input("Ingrese el numero de clases: "))
asistencia = int(input("Por favor indique a cuantas clases asitió: "))
porcentaje = asistencia / clases

if porcentaje > 0.75:
    print("El estudiante puede hacer el examen")
else:
     tieneExcusa = input("¿El estudiante tiene excusa médica?: ").lower
     if tieneExcusa == "si" or "sí":
         print("El estudiante puede presentar el examen")
     else:
         print("El estudiante no puede presentar el examen")

print("Su porcentaje de asistencia es del {:.2f}%".format(porcentaje * 100))