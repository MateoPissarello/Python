
from Persona import Persona #Si colocamos * importamos todas las clases que se encuentran en un archivo

print("Creación objetos".center(30,"*"))
persona1 = Persona("Carla", "Gomez", "30")
persona1.mostrar_detalle()

#Destructor de objetos en python
print("Eliminación objetos".center(30,"*"))
del persona1
