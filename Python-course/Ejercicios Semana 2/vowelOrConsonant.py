
vowelsList = ["a", "e", "i", "o", "u"]
consonantsList = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "x", "z", "w", "y"]

getChar = input("Por favor digite una letra: ").lower()

if getChar in vowelsList:
    print("Esto es una vocal")
elif getChar in consonantsList:
    print("Esto es una consonante")
else:
    print("Esto no es una letra")