# Diccionarios (dict) (key,keyvalue)
diccionario = {
    "IDE":"integraded Development Environment",
    "OOP":"Object Oriented Programming",
    "DBMS":"Database Management System"
}
print(diccionario)

#largo
print(len(diccionario))
#Acceder a un elemento en un diccionario (key)
print(diccionario["IDE"])
#Otra forma de recuperar un elemento
print(diccionario.get("OOP"))
#Modificar elementos
diccionario["IDE"] = "integrated development environment"
print(diccionario)
# Recorrer los elementos de un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

#comprobar existencia de algun elemento
print("IDE" in diccionario)

#agregar un elemento 
diccionario["PK"] = "Primary Key"
print(diccionario)

#remover un elemento
diccionario.pop("DBMS")
print(diccionario)

#limpiar
diccionario.clear()
print(diccionario)

#eliminar
del diccionario
#print(diccionario)

#unir diccionarios
dict_ports1 = {22:"SSH", 80:"Http"}
dict_ports2 = {53:"DNS", 443:"https"}
print(dict_ports1)
dict_ports1.update(dict_ports2)
print(dict_ports1)

#comparar diccionarios
a = {123:"Rojas", 87:"Rosas"} == {87:"Rosas", 123:"Rojas"}
print(a)
print({"Rosas":123} != {"rosas":123})
b = {123:"Rosas", 87:"rojas"} == {"Rosas":123, 87:"rojas"}
print(b)

#acceder a un value con la key dada
puertos = {22:"SSH", 23:"Telnet", 80:"HTTP", 3306:"MySQL"}
protocolo = puertos[22]
print(protocolo)
#puertos[443] #no hay una key 443 por lo que genera un error

#Eliminar un elemento con la llave dada
puertos = {22:"SSH", 23:"Telnet", 80:"HTTP", 3306:"MySQL"}
print(puertos)
del puertos[23]
print(puertos)

#Consultar un diccionario
puertos = {80:"HTTP", 23:"SMTP", 443:"HTTPS"}
if 80 in puertos:
    print("yes")
if 110 not in puertos:
    print("no")
else:
    print("yes")

#iterar un diccionario para obtener las llaves
dict_ports = {22:"SSH", 23:"telnet", 80:"Http"}
for key in dict_ports:
    print(key)

#iterar para obtener llaves y valor
dict_ports = {22:"SSH", 23:"telnet", 80:"Http"}
for k,v in dict_ports.items():
    print(k, "->", v)

#obtener el valor de un  ́ıtem a partir de la llave con el método get. 
dict1 = {"a":1, "b":2, "c":3}
print(dict1.get("a"))
print(dict1.get("d", "clave no encontrada."))

#obtiene la máxima/mínima clave de los ítems en el diccionario.
puertos = {80:"HTTP", 23:"SMTP", 443:"HTTPS"}
print(max(puertos))
print(min(puertos))

#lista de claves y valores
dict1 = {"a":1, "b":2, "c":3}
print(list(dict1.keys()))
print(list(dict1.values()))

#convertir listas de listas a diccionarios
puertos = [[80, "http"], [20, "ftp"], [23, "telnet"]]
d_port = dict(puertos)
print(d_port)
puertos = [(20, "ftp"), (80, "http"), (23, "telnet")]
d_port = dict(puertos)
print(d_port)

#metodo copy
port = {80:"HTTP", 23:"SMTP", 443:"HTTPS"}
copy_port = port.copy()
false_copy = port
print(port)
print(copy_port)
print(false_copy)