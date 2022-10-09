def calcular_BMI(peso,altura):
    pesokg = peso * 0.45
    alturam = altura * 0.025
    calculo = pesokg / (alturam ** 2)
    calculo = round(calculo,2)
    print(calculo)
    return calculo
peso_lb = 154
altura_inch =70.86 

calcular_BMI(peso_lb,altura_inch)
