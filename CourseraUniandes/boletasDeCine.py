
def calcular_costo_boletas(cantidad_boletas:int, tipo_sala:str, hora_pico:bool, pago_tarjeta_cinema:bool, reserva:bool):
    tarifaDinamix = 18800
    tarifa3D = 15500
    tarifa2D = 11300
    total_a_pagar = 0
    if pago_tarjeta_cinema == True:
        tarifaDinamix = tarifaDinamix - (tarifaDinamix * 0.05)
        tarifa3D = tarifa3D - (tarifa3D * 0.05)
        tarifa2D = tarifa3D - (tarifa3D * 0.05)
    if reserva == True:
        total_a_pagar += cantidad_boletas * 2000
    if hora_pico == True:
        tarifaPicoDinamix = tarifaDinamix + (tarifaDinamix * 0.5)
        tarifaPico3D = tarifa3D + (tarifa3D * 0.25)
        tarifaPico2D = tarifa2D + (tarifa2D * 0.25)
    if tipo_sala == "Dinamix" and hora_pico == True:
        total_a_pagar += tarifaPicoDinamix * cantidad_boletas
    elif tipo_sala == "Dinamix" and hora_pico == False:
        if cantidad_boletas > 3:
            tarifaDinamix - 500
        tarifaDinamix = tarifaDinamix - (tarifaDinamix * 0.1)
        total_a_pagar += tarifaDinamix * cantidad_boletas
    if tipo_sala == "2D" and hora_pico == True:
        total_a_pagar += tarifaPico2D * cantidad_boletas
    elif tipo_sala == "2D" and hora_pico == False:
        if cantidad_boletas > 3:
            tarifa2D - 500
        tarifa2D = tarifa2D - (tarifa2D * 0.1)
        total_a_pagar += tarifa2D * cantidad_boletas       
    if tipo_sala == "3D" and hora_pico == True:
        total_a_pagar += tarifaPico3D * cantidad_boletas
    elif tipo_sala == "3D" and hora_pico == False:
        if cantidad_boletas > 3:
            tarifa3D - 500
        tarifa3D = tarifa3D - (tarifa3D * 0.1)
        total_a_pagar += tarifa3D * cantidad_boletas
    return round(total_a_pagar)


calcular_costo_boletas(2,"Dinamix",1,0,1)