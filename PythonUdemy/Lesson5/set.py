#set (no guarda un orden)
planetas = {"Marte", "Júpiter", "Venus"}
print(planetas)
#largo
print(len(planetas))
# revisar si un elemento esta presente 
print("Marte" in planetas)
#agregar un elemento a nuestro set
planetas.add("Tierra")
print(planetas)
#No se pueden duplicar elementos
planetas.add("Tierra")
print(planetas)
#Eliminar un elemento posiblemente arrojando un error
planetas.remove("Tierra")
print(planetas)
#Eliminar un elemtno sin arrojar error
planetas.discard("Júpiters")
print(planetas)
#limpiar set
planetas.clear()
#eliminar el set
del planetas
print(planetas)