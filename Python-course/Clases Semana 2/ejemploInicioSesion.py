
#pedirle al usuario que ingrese su contraseña 
#si la contraseña coincide con storedPassword, mostrarle un mensaje de inicio de sesion correcto

#Si la contraseña no coincide, mostrarle un mensaje de error
#y perdirle la contraseña nuevamente
maxRetries = 3
storedPassword = "123abc"
userPassword = input("Por favot ingrese su contraseña: ")
count = 1

while storedPassword != userPassword and count < maxRetries:
    print("Las contraseñas no coinciden")
    count = count + 1
    print("valor del contador", count)
    userPassword = input("Por favor ingrese nuevamente la contraseña: ")

if count >= maxRetries:
    print("Te equivocaste más de 3 veces. Te hemos bloqueado.")
else:
    print("¡Inicio de sesión exitoso!")
