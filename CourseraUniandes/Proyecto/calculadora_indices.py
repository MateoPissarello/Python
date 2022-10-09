def calcular_IMC(peso:float, altura:float):
    IMC = peso / (altura ** 2)
    IMC = round(IMC,2)
    return IMC

def calcular_porcentaje_grasa(peso:float, altura:float, edad:int, valor_genero:float):
    IMC = calcular_IMC(peso,altura)
    porcentaje_grasa = 1.2 * IMC + 0.23 * edad - 5.4 - valor_genero
    porcentaje_grasa = round(porcentaje_grasa,2)
    return (f"{porcentaje_grasa}%")

def calcular_calorias_en_resposo(peso:float, altura:float, edad:int, valor_genero:float):
    calorias_en_reposo = (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero
    calorias_en_reposo = round(calorias_en_reposo,2)
    return calorias_en_reposo

def calcular_calorias_en_actividad(peso:float, altura:float, edad:int, valor_genero:int, valor_actividad:float):
    TMB = calcular_calorias_en_resposo(peso,altura,edad,valor_genero)
    TMB_en_actividad = TMB * valor_actividad
    TMB_en_actividad = round(TMB_en_actividad,2)
    return TMB_en_actividad

def consumo_calorias_recomendado_para_adelgazar(peso:float, altura:float, edad:int, valor_genero:int):
    TMB = calcular_calorias_en_resposo(peso,altura,edad,valor_genero)
    adelgazarVmin = TMB * 0.80
    adelgazarVmin = round(adelgazarVmin,2)
    adelgazarVmax = TMB * 0.85
    adelgazarVmax = round(adelgazarVmax,2)
    return (f"Para adelgazar es recomendado que consumas entre: {adelgazarVmin} y {adelgazarVmax} calorías al día.")



