#Definir una lista de str
nombres = ["Juan","Karla", "Ricardo", "María"]
#imprimir la lista de nombres
print(nombres)
#acceder a los elementos de una lista
print(nombres[0])
print(nombres[1])
# acceder a los elementos de manera inversa
print(nombres[-1])
print(nombres[-2])
# imprimir un rango
print(nombres[0:2]) #Imprime los elementos de la lista del 0 al 2 sin incluir el 2
#Ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3])
#Desde el indice indicado hasta el final de la lista
print(nombres[1: ])
#Cambiar un valor especificando un indice
nombres[3] = "Ivone"
print(nombres)
#iterar una lista
for name in nombres:
    print(name)
else:
    print("No existen mas nombres en la lista")
#preguntar el largo de una lista
print(len(nombres))
# agregar un elemento
nombres.append("Lorenzo")
print(nombres)
#insertar un elemento en un indice en especifico
nombres.insert(1,"Octavio")
print(nombres)
#remover un elemento
nombres.remove("Octavio")
print(nombres)
# remover el ultimo valor agregado
nombres.pop()
print(nombres)
#eliminar un elemento en un indice indicado
del nombres[0]
print(nombres)
#limpiar todos los elementos de la lista
nombres.clear()
print(nombres)
#borrar la lista por completo 
del nombres
print(nombres)