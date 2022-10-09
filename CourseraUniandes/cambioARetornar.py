
def  calcular_cambio(cambio):
    lista = []
    A,B,C,D = 0,0,0,0
    while cambio != 0:  
        if cambio > 500 and cambio // 500 >= 1:
            x = cambio // 500 # Cantidad de veces que cabe el cambio en 500
            cambio -= (x * 500) #Se resta el valor de cambio
            A = x 
            #x = str(A)
        elif cambio < 500 and cambio // 200 >= 1:
            x = cambio // 200 # Cantidad de veces que cabe el cambio en 500
            cambio -= (x * 200) #Se resta el valor de cambio 
            B = x
            #x = str(B)
        elif cambio < 200 and cambio // 100 >= 1:
            x = cambio // 100 # Cantidad de veces que cabe el cambio en 500
            cambio -= (x * 100) #Se resta el valor de cambio 
            C = x
            #x = str(C)
        elif cambio < 100 and cambio // 50 >= 1:
            x = cambio // 50 # Cantidad de veces que cabe el cambio en 500
            cambio -= (x * 50) #Se resta el valor de cambio 
            D = x
            #x = str(D)        
    lista.append(f"{A},{B},{C},{D}")
    listaStr = "".join(lista)
    listaStr = listaStr.rstrip(",")
    return listaStr

print(calcular_cambio(200))


        




        



