
# Los primeros dos años de perro equivalen a 10.5 años humanos, depues cada año equivale a 4 años humanos

from re import I


dogsAge = float(input("Por favor digite los años que tiene su perro: "))

inHuman = 10.5

if dogsAge >= 2:
    inHuman = (10.5 * 2) + ((dogsAge - 2) * 4)
    print("La edad de su mascota en años humanos es de ", inHuman)

else:
    inHuman = 10.5
    print("La edad de su mascota en años humanos es de ", inHuman)


