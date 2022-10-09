
n = 25
m = 30
def Menu():

    print("1.Tablero")
    print("2. Mitad Superior")
    print("3. Mitad inferior")
    opcion = int(input("\t\t Ingrese la opcion\n"))
    if opcion == 1:
        imprimirTablero()

    if opcion == 2:
        imprimirMitadSuperior()

    if opcion == 3:
        imprimirMitadInferior()
    if opcion == 4:
        imprimirCirculo()

    elif opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4:
        print("\t\t Opción invalida\n")
        Menu()


def imprimirTablero():
    global n
    global m
    for i in range(n):
        for j in range(m):
            if i % 2 != 0:
                print(" ❐", end="")
            if i % 2 == 0:
                print("❐ ", end="")
        print("")


def imprimirMitadSuperior():
    global n
    global m
    for i in range(n):
        for j in range(m - (i + 2)):
            if i % 2 != 0:
                print("  ❐", end="")
            if i % 2 == 0:
                print("❐  ", end="")

        print("")


def imprimirMitadInferior():
    global n
    global m
    for i in range(n + 1):
        espacio = m - i
        print("  " * espacio + " ❐" * i)

def imprimirCirculo():
    radio = int(input("Ingrese el radio: "))
    for i in range(radio):
        for j in range(radio):
            if i == 0 and j == 2:
                print(" ", end="")
            else:
                print("❐  ", end="")
        print(" ")


Menu()