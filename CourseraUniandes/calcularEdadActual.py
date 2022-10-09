from datetime import datetime
#navidad = datetime.strptime("2021-12-25", "%Y-%m-%d")
#fin_anio = datetime.strptime("2021-12-31", "%Y-%m-%d")
#diferencia = fin_anio-navidad
#print(f"La diferencia es de {diferencia.days} días y {diferencia.m} segundos. La diferencia total es de {diferencia.total_seconds()} segundos")


def calcular_edad(dia_nacio:int, mes_nacio:int, anio_nacio:int, dia_actual:int, mes_actual:int, anio_actual:int):
    fechaNacimiento = str(anio_nacio) + ("-") + str(mes_nacio) + ("-") + str(dia_nacio)
    fechaActual = str(anio_actual) + ("-") + str(mes_actual) + ("-") + str(dia_actual)
    fechaNacimiento = datetime.strptime(fechaNacimiento, "%Y-%m-%d")
    fechaActual = datetime.strptime(fechaActual, "%Y-%m-%d")
    diferencia = fechaActual - fechaNacimiento
    dias = diferencia.days
    while dias != 0:
        anios,meses,diasR = 0,0,0
        if dias > 365 and dias // 365 >= 1:
            anios = dias // 365
            dias -= ( anios * 365)
            anios = str(anios)
        elif dias < 365 and dias // 30 >= 1:
            meses = dias / 30
            dias -= (meses * 30)
            meses = str(meses)
        else:
            diasR = dias
            dias -= diasR
            diasR = str(diasR)

    print(f"{anios}, {meses}, {diasR}")




calcular_edad(20,11,1986,16,10,1987)