def calcularIva(precioProducto:int) -> int:
    iva = precioProducto * 0.19
    productoFinal = iva + precioProducto
    return productoFinal

precio = int(input("Digite el precio del producto: "))
productoFinal = calcularIva(precio)
print(f"El iva es de {productoFinal} pesos") 
#print("El precio final con el IVA incluido es de $",productoFInal)


    