numero=int(input("Introduzca el número natural: "))
while numero <= 0:
    print("Error introduzca un número natural")
    numero=int(input("Introduzca el numero natural: "))
if numero == 2:
    primo = True
else:
    for i in range(2,numero):
        if (numero%i == 0):
            primo = False
            break
        else:
            primo = True
if primo:
    print(f"El número {numero} es primo")
else: 
    print(f"El numero {numero} no es primo")        