# se le pide al usuario que digite un numer0, este numero tambien va a ser el limite de la tabla
nTabla = int(input("Seleccione de que numero desea la tabla: "))
count = 0

while count < nTabla:
    count += 1
    multiplicacion = nTabla * count
    print(multiplicacion)