#A diferencia de las listas, estas no son mutables

#Definir una tupla
frutas = ("Naranja", "Plátano", "Guayaba") #para diferenciar una tupla de un str, si solo tiene un elmento se debe colocar una "," al final
print(frutas)
#saber el largo
print(len(frutas))
#Acceder a un elemento
print(frutas[0])
#Navegacion inversa
print(frutas[-1])
#Acceder a un rango
print(frutas[0:1]) #sin incluir el ultimo indice
#recorrer elementos
for fruta in frutas:
    print(fruta, end= " ")
#cambiar un valor de una tupla
#frutas[0] = "Pera"
frutasLista = list(frutas)
frutasLista[0] = "Pera"
frutas = tuple(frutasLista)
print("\n",frutas)
#eliminar la tupla por completo
del frutas
print(frutas)


