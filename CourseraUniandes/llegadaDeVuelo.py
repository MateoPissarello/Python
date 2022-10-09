
def calcular_horario_llegada(hora_salida,minuto_salida,segundo_salida,duracion_horas,duracion_minutos,duracion_segundos):
    hora_de_llegada = hora_salida + duracion_horas
    if hora_de_llegada > 23:
        hora_de_llegada = hora_de_llegada - 24
    minuto_de_llegada = minuto_salida + duracion_minutos
    if minuto_de_llegada > 59:
        minuto_de_llegada -= 60
        hora_de_llegada +=1
    segundos_de_llegada = segundo_salida + duracion_segundos
    if segundos_de_llegada > 59:
        segundos_de_llegada -= 60
        minuto_de_llegada +=1
    if hora_de_llegada == 24:
        hora_de_llegada = 0
    string = str(f"{hora_de_llegada}:{minuto_de_llegada}:{segundos_de_llegada}")
    return print(string)


calcular_horario_llegada(14,15,20,0,52,10)