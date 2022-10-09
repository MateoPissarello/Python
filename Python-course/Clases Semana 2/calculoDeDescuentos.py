
# precio de base de los huevos = 1800
# precio de base de las arepas = 5000
# si alguien compra mas de 10 canastas, el precio 1000

#si alguien compra mas de 10 canastas de huevos y ademas compra 10 paquetes de arepas
#el precio de los huevos es 800 y el de las arepas es 2000

#paso 1: preguntar cuantos huevos quiere comprar la persona
cantidadHuevos = int(input("Digite la cantidad de canastas de huevos que desea comprar: "))
#paso 2: preguntar si la persona quiere comprar arepas
quiereArepas = input("¿Usted desea llevar arepas?: ").lower()
#paso 3: si la persona quiere comprar arepas, preguntarle cuántas
if quiereArepas == "si" or quiereArepas == "sí":
    cantidadArepas = int(input("Digite la cantidad de paquetes de arepas que quiere comprar: "))
else:
    cantidadArepas = 0
#paso 3; calcular el total de la compra

if cantidadArepas > 10 and cantidadHuevos > 10:
    precioDeHuevos = 800
    precioDelasArepas = 2000

if cantidadHuevos > 10:
    precioDeHuevos = 1000
    precioDelasArepas = 5000

else:
    precioDeHuevos = 1800
    precioDelasArepas = 5000

subTotal = precioDeHuevos * cantidadHuevos + precioDelasArepas * cantidadArepas
print(f"El total de su compra es ${subTotal}")

#Condiciones adicionales que se deben cumplir:
#si el total de la compra es mayor a 50.000, y solo estoy comprando un producto, dar un descuento adicional del 10%´
# if  subTotal > 50000 and (cantidadHuevos == 0 or cantidadArepas == 0):
# descuento = subTotal * 0.10
# totalCompra = subTotal - descuento

# #si el total de la compra es mayor a 50.000 y ademas estan comprando huevos y arepas, el descuento no es de 10% sino es del 15%
# elif subTotal > 50000 and (cantidadArepas > 0 and cantidadHuevos > 0):
# descuento = subTotal * 0.15
# totalCompra = subTotal - descuento
# else:
# descuento = 0
# totalCompra = subTotal

# print(f"Tuvo un descuento adicional en la compra de ${descuento} pesos")
# print(f"El nuevo precio de su compra es ${totalCompra}")

#mostrarle al usuario el total de la compra y tambien el total del descuento

#version if anidado
descuento = 0
if subTotal > 50000:
    if cantidadArepas == 0 or cantidadHuevos == 0:
        descuento = subTotal * 0.10
    else:
        descuento = subTotal * 0.15

total = subTotal - descuento


