import random
tamañoFilas = int(input("Ingrese el tamaño de las filas: "))
tamañoColumnas = int(input("Ingrese el tamaño de las columnas: "))
def generarMatriz():
    listaCoordenadas = []
    listaBasuras = []
    filas = tamañoFilas
    columnas = tamañoColumnas
    matriz = []
    for i in range(filas):
        matriz.append([0]*columnas)
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = random.randrange(0,11)
    return matriz

matriz = generarMatriz()
print(matriz)

def generarCoordenadas():
    listaCoordenadas = []
    filas = tamañoFilas
    columnas = tamañoColumnas
  #Añadir una hoja si el randint es mayor o igual a 5
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] >= 5:
                coordenadas = (i,j)
                listaCoordenadas.append(coordenadas)
    return listaCoordenadas

def generarBasuras():
    listaBasuras = []
    filas = tamañoFilas
    columnas = tamañoColumnas
    for i in range(filas):
        for j in range(columnas):
           if matriz[i][j] >= 5:
                basura = "basuras"
                listaBasuras.append(basura)
    return listaBasuras
listaCoordenas = generarCoordenadas()
print(listaCoordenas)
listaBasuras = generarBasuras()
print(listaBasuras)


coordenadas = (0,0)
if coordenadas in listaCoordenas:
    print("La coordena esta en la lista")
else:
    print("La coordenada no esta en la lista")