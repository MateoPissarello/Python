
def imprimirTablero(n,m):
    for i in range(n):
        for j in range(m):
            if (i+j) %2 == 0:
                print("#  ", end="")
            else:
                print("  ", end="")
        print("")

imprimirTablero(25,25)

def imprimirDiagonalSuperior(n,m):
    for i in range(n):
        for j in range (m-i):
            if (i+j) % 2 ==0:
                print("#  ", end="")
            else:
                print("  ", end="")
        print("  ")

print("")

imprimirDiagonalSuperior(5,5)

def imprimirDiagonaInferior(n,m):
    for i in range(n):
        for j in range(m-i):
            if (i+j) % 2 == 0:
                print("  ", end="")
            else:
                print("  ", end="")
        for j in range(i):
            if (i+j) % 2 == 0:
                print("#  ", end="")
print("")
imprimirDiagonalSuperior(15,15)