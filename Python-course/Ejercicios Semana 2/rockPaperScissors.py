
countP1 = 0
countP2 = 0

while countP1 < 2 or countP2 < 2:
    player1 = input("Ingrese R, P o S: ").upper()
    player2 = input("Ingrese R, P o S: ").upper()
    if player1 == player2:
        print("Empate")

    if player1 == "R" and player2 == "S":
        print("El jugador 1 gana")
        countP1 += 1
    elif player2 == "R" and player1 == "S":
        print("El jugador 2 gana")
        countP2 += 1

    if player1 == "P" and player2 == "R":
        print("El jugador 1 gana")
        countP1 += 1
    elif player2 == "P" and player1 == "R":
        print("El jugador 2 gana")
        countP2 += 1

    if player1 == "S" and player2 == "P":
        print("El jugador 1 gana")
        countP1 += 1
    elif player2 == "S" and player1 == "P":
        print("El jugador 2 gana")
        countP2 += 1

        print("El jugador 1 ha ganado", countP1)
        print("EL jugador 2 ha ganado", countP2)

if countP1 == 2:
    print("El jugador 1 ganó 2 veces")
if countP2 == 2:
    print("El jugador 2 ganó 2 veces")