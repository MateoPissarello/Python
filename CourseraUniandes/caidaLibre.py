import math as m

def vel_en_caida_libre(altura:float):
    vf = m.sqrt(0**2 +(2 * 9.8) * altura)
    return vf
vel_en_caida_libre(200)