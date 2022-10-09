def movimiento_robot(orientacion_actual:str, giro_1:str, giro_2:str, giro_3:str):
    list = [giro_1, giro_2, giro_3]
    for giro in list:
        if orientacion_actual == "N" and giro == "L":
            orientacion_actual = "W"
            continue
        elif orientacion_actual == "N" and giro == "R":
            orientacion_actual = "E"
            continue
        elif orientacion_actual == "N" and giro == "H":
            orientacion_actual = "S"
            continue
        elif orientacion_actual == "N" and giro == ".":
            orientacion_actual = "N"
            continue
        if orientacion_actual == "S" and giro == "L":
            orientacion_actual = "E"
            continue
        elif orientacion_actual == "S" and giro == "R":
            orientacion_actual = "W"
            continue
        elif orientacion_actual == "S" and giro == "H":
            orientacion_actual = "N"
            continue
        elif orientacion_actual == "S" and giro == ".":
            orientacion_actual = "S"
            continue
        if orientacion_actual == "W" and giro == "L":
            orientacion_actual = "S"
            continue
        elif orientacion_actual == "W" and giro == "R":
            orientacion_actual = "N"
            continue
        elif orientacion_actual == "W" and giro == "H":
            orientacion_actual = "E"
            continue
        elif orientacion_actual == "W" and giro == ".":
            orientacion_actual = "W"
            continue
        if orientacion_actual == "E" and giro == "L":
            orientacion_actual = "N"
            continue
        elif orientacion_actual == "E" and giro == "R":
            orientacion_actual = "S"
            continue
        elif orientacion_actual == "E" and giro == "H":
            orientacion_actual = "W"
            continue
        elif orientacion_actual == "E" and giro == ".":
            orientacion_actual = "E"
            continue
    return print(orientacion_actual)
    
movimiento_robot("E",".","L","L")