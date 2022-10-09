from struct import pack


def calcularImpuesto(pagoSinImpuesto, Impuesto):
    pagoTotal  = pagoSinImpuesto + pagoSinImpuesto * (impuesto/100)
    return pagoTotal
pagoSinImpuesto = float(input("Proporcione el pago sin impuesto: "))
impuesto = float(input("Proporcione el monto del impeusto: "))
pagoTotal = calcularImpuesto(pagoSinImpuesto, impuesto)
print(f"Pago con impuesto: {pagoTotal}")