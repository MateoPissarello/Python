#El asteristco indica que no sabemos 
# cuantos nombres van a pasar como parametro 
# por nuestra lista, esto los convertira en una tupla
#Normalmente se encuentra con el nombre "*args"
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)
listarNombres("Juan", "Daniela", "Mateo", "Carla", "Axel", "Lulu", "Camilo")