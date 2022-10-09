mi_lista = []
mi_lista.append(5) # Agrega un elemento al final de la lista
mi_lista.append(27)
mi_lista.append(3)
mi_lista.append	(12)
print(mi_lista)

mi_lista.insert(1,12)# Instera un elemento en una posición dada de la lista
print(mi_lista)
print(mi_lista.count(12)) # Cuenta cuántas veces aparece un elemento en la lista

mi_lista.extend([5,9,5,11]) # Inserta una lista entera al final de la lista
print(mi_lista)

print(mi_lista.index(9)) #Busca el índice(posición) de un elemento en la lista

mi_lista.reverse() #Invierte los elementos de una lista
print(mi_lista)

mi_lista.sort() #Ordena los elementos de mayor a menor en una lista o en orden alfabetico 
print(mi_lista)

mi_lista.remove(12) #Remueve la primera ocurrencia de un elemento dado de la lista
print(mi_lista)

otra_lista = mi_lista.copy() # Crea una nueva lista que es una copia de la lista original
print(otra_lista)

eliminado = mi_lista.pop(4) # Remueve un elemento de una posición dada de la lista y lo devuelve
print(mi_lista)
print(eliminado)

mi_lista.clear() #Elimina todos los elementos de una lista
print(mi_lista)