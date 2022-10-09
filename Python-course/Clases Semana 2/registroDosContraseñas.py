contraseñasIguales = False

while contraseñasIguales == False:
    contraseña1 = input("Contraseña: ")
    contraseña2 = input("Ingrese nuevamente la contraseña: ")
    if contraseña1 == contraseña2:
        contraseñasIguales = True
    else:
        print("Las contraseñas con diferentes. Por favor ingreselas nuevamente.")
        
print("Registro exitoso.")