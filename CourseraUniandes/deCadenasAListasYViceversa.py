#LISTA A CADENA
cadena = "uno dos tres"
print(cadena)
lista = cadena.split()
print(lista)

cadena = "Hola, cómo, estás?"
lista = cadena.split(",")
print(lista)

#CADENA A LISTA
a = " ".join(["uno","dos","tres"])
print(a)
a = "--".join(["uno","dos","tres"])
print(a)
a = ":".join(["uno","dos","tres"])
print(a)

#CONSTURIR LISTA CON list

a = list(range(1,4))
print(a)

a = list("1289463027494") #Toca pasar el numero como str
print(a)
a = list("la casa blanca")
print(a)
