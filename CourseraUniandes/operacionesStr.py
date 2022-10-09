def comparar_cadenas(palabra1:str, palabra2:str) -> None:
    if (palabra1 == palabra2):
        print("Las palabras son iguales")
    elif (palabra1 < palabra2):
        print("La palabra",palabra1,"es menor que la palabra",palabra2)
    else:
        print("La palabra",palabra1,"es mayor que la palabra", palabra2)

comparar_cadenas("alma", "blanca")

#El operador un comprueba si una cadena forma parte de otra o no de otra cadena
print("-"*30)
print("\tOperador in")
print("n" in "manzana")
print("p" in "manzana")
print("za" in "manzana")
print("pa" in "manzana")
print("a" in "a")
print("manzana" in "manzana")
print("" in "a")
print("" in "manzana")

#Operador not in, opuesto lógico de in
print("-"*30)
print("\tOperador not in")
print("X" not in "manzana")

"""funciones de cadenas"""
a = "Vaca"
print(a.lower()) #devuelve la cadena a en minúscula
print(a.upper()) #devuelve la cadena a en mayúscula
print(a.title()) #devuelve la cadena empezando por mayúscula
print(a.swapcase()) #devuelve una nueva cadena con los caracteres en minúscula convertidos en mayúscula y viceversa

a ="Una Vaca caminando por la pradera"
b = a.replace("pradera", "montaña")
print(b)



