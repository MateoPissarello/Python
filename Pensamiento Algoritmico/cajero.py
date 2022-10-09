from termcolor import colored
import colorama as cl
import time
cl.init()

saldo = 1000000
opcion = 0
cien = 0
cincuenta = 0
veinte = 0
diez = 0
user = 1234
password = 4321


#else:
#    print("Usted ha ingresado una opcion invalida")
def imprimirMenu():
    print(colored("\t\tBIENVENIDO AL CAJERO DE @ELMATY\n", "red"))
    print(colored("1. Consultar el saldo", "cyan"))
    print(colored("2. Consignar", "blue"))
    print(colored("3. Retirar", "cyan"))
    print(colored("4. Salir", "blue"))

def imprimirSaldo():
    global saldo
    print(colored(f"\nSu saldo es de {saldo}", 'green', attrs=["bold"]))

def consignar(valor):
    global saldo
    saldo += valor
    return saldo
def contarBilletes(valor,denominacion):
    calcularVecesQueCabe = valor / denominacion
    return calcularVecesQueCabe
def retirar(cantidad):
    global saldo
    mod = cantidad % 10000
    if cantidad > saldo and mod != 0:
        print("\nNo puede retirar esa cantidad")
    else:
        if mod == 0:
            saldo -= cantidad 
            if cantidad >= 100000 and cantidad // 100000 >= 1:
                cien = contarBilletes(cantidad,100000) #Cantidad de veces que cabe 100000 en la cantidad a retirar
                cantidad -= cien * 100000
            if cantidad < 100000 and cantidad // 50000 >= 1:
                cincuenta = contarBilletes(cantidad, 50000)
                cantidad -= cincuenta * 50000
            if cantidad < 50000 and cantidad // 20000 >= 1:
                veinte = contarBilletes(cantidad, 20000)
                cantidad -=  veinte * 20000
            if cantidad < 20000 and cantidad // 10000 >= 1:
                diez = contarBilletes(cantidad,10000)
                cantidad -= diez * 10000
        return saldo

def validarUsuario(usuario, contrasenia):
    bandera = False
    if (usuario == user and contrasenia == password):
        bandera = True
    return bandera

def exit():
    print(colored("Gracias por usar nuestros servicios", "green"))
    time.sleep(2)
    print(colored("Saliendo . . .", "red", attrs=["bold"]))
    time.sleep(1)
    print("-" * 30)
    time.sleep(1)
    print(cl.ansi.clear_screen())

def validarOpcion():
    decision = input("\nDesea continuar? (s/n): ")
    if decision == 's':
        main()
    else:
        exit()
def main():
    usuario1 = int(input(colored("Por favor ingrese el usuario: ", 'green', attrs=["bold"])))
    password2 = int(input(colored("Por favor ingrese la contraseña: ", 'green', attrs=["bold"])))
    if validarUsuario(usuario1, password2):
        imprimirMenu()
        opcion = int(input(colored("\nIngrese la opcion que desea realizar: ", "red" , attrs =["bold"])))
        match opcion:
            case 1:
                imprimirSaldo()
                validarOpcion()
            case 2:
                cantidad = int(input(colored("Digite la cantidad a consignar: ", "green")))
                consignar(cantidad)
                print(f"\nLa cantidad consignada fue de {cantidad}\n")
                print("\nEl nuevo saldo es de " + colored(str(saldo), "green", attrs=["bold"]))
                print("-" * 30)
                validarOpcion()
            case 3:
                cantidad = int(input(colored("Ingrese la cantidad a retirar: ", "green")))
                if cantidad > saldo or cantidad % 10000 != 0 or cantidad <= 0:
                    print(colored("\nNo puede retirar esa cantidad", "red", attrs=["bold"]))
                else:

                    print("\nRetirando...")
                    retirar(cantidad)
                    if cien > 0:
                        print(f"\n{cien} billete/s de cien\n")
                    if cincuenta > 0:
                        print(f"\n{cincuenta} billete/s de cincuenta\n")
                    if veinte > 0:
                        print(f"\n{veinte} billete/s de veinte\n")
                    if diez > 0:
                        print(f"\n{diez} billete)s de diez\n")
                    print("\nEl nuevo saldo es de " + colored(str(saldo), "green", attrs=["bold"]))
                    #print(f"\nLa cantidad retirada fue de {cantidad}\n")
                print("-" * 30)
                validarOpcion()
            case 4:
                exit()
            case _:
               print(colored("\nOpcion invalida", "red", attrs=['bold']))
    else:
        print("\nSus credenciales son invalidas . . .", "red", attrs=['bold'])

main()


