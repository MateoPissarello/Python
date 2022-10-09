#Tamnbien conocido como slicing, excluye el ultimo indice en el rango dado
s = "Piratas del Caribe"
x = s[0:7] 
print(x)
y = s[8:11]
print(y)
z = s[12:18]
print(z)

fruta = "manzana"
inicio = fruta[:3]
print(inicio)
final = fruta[3:]
print(final)
completa = fruta[:]
print(completa)
avance1 = fruta[::1]
print(avance1)
avance2 = fruta[::2]
print(avance2)
inverso = fruta[::-1]
print(inverso) 